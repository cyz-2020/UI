import unittest

from config import Config
from page.login import Login
from util.logger import Logger

# log = Logger().logger


class BaseCaseCls(unittest.TestCase):
    driver = None
    retry = 0

    @classmethod
    def setUpClass(cls) -> None:
        # cls.case_id = cls.__class__.__name__
        cls.case_id = cls.__name__
        lg = Login()
        try:
            cls.driver = lg.login()
        except Exception as e:
            if lg.driver:
                lg.driver.quit()
                # log.info('{}登录失败！原因：{}'.format(cls.case_id, e.__str__()))
            assert 0, "{} 登录失败! 原因: {}".format(cls.case_id, e.__str__())

    @classmethod
    def _clean(cls):
        if cls.driver:
            cls.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        cls._clean()
