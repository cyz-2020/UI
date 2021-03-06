import unittest
from config import Config
from util.logger import Logger


def _isnotsuite(test):
    try:
        iter(test)
    except TypeError:
        return True
    return False


class Suite(unittest.TestSuite):
    logger = Logger().logger

    def run(self, result, debug=False):
        topLevel = False

        if getattr(result, '_testRunEntered', False) is False:
            result._testRunEntered = topLevel = True

        for index, test in enumerate(self):
            retry = getattr(test, "retry", Config.RETRY)
            if result.shouldStop:
                break

            for i in range(1, retry + 2):
                if _isnotsuite(test):
                    self._tearDownPreviousClass(test, result)
                    self._handleModuleFixture(test, result)
                    self._handleClassSetUp(test, result)
                    result._previousTestClass = test.__class__
                    if (getattr(test.__class__, '_classSetupFailed', False) or
                            getattr(result, '_moduleSetUpFailed', False)):
                        continue
                self.logger.info("用例: {}正在尝试第{}次运行!".format(test.__class__.__name__, i))
                if not debug:
                    test(result)
                else:
                    test.debug()
                if i < retry + 1:
                    # 重试判断  可以继续优化
                    error, fail, skip = None, None, None
                    skip_id = [x.get("case_id") for x in result.skipped]
                    fail_id = [x.get("case_id") for x in result.failures]
                    error_id = [x.get("case_id") for x in result.errors]
                    if test.case_id in fail_id:
                        fail = fail_id.index(test.case_id)
                    if test.case_id in error_id:
                        error = error_id.index(test.case_id)
                    if test.case_id in skip_id:
                        skip = skip_id.index(test.case_id)
                    if error is None and fail is None:
                        # 说明没有失败or错误, 停止重试
                        break
                    elif error is not None:
                        self.logger.warning("用例: {} 第{}次失败 原因: {}".format(test.__class__.__name__,
                                                                          i, str(result.errors[error]['msg'])))
                        del result.errors[error]
                    elif fail is not None:
                        self.logger.warning("用例: {} 第{}次失败 原因: {}".format(test.__class__.__name__,
                                                                          i, str(result.failures[fail]['msg'])))
                        del result.failures[fail]
                    elif skip is not None:
                        self.logger.warning("用例: {} 第{}次失败 原因: {}".format(test.__class__.__name__,
                                                                          i, str(result.skipped[skip]['msg'])))
                    result._previousTestClass = test.__class__
                    continue
            if self._cleanup:
                self._removeTestAtIndex(index)

        if topLevel:
            self._tearDownPreviousClass(None, result)
            self._handleModuleTearDown(result)
            result._testRunEntered = False
        return result


if __name__ == '__main__':
    unittest.main()
