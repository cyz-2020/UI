import logging
import time
import unittest
from unittest import skip

from config import Config
from page.base import Location
from page.index import Index
from tests.base_case_callcenter import BaseCaseCallCenter
from util.decorator import screenshot
from util.logger import Logger

Log = Logger().logger


class CallCenterLogin(BaseCaseCallCenter):
    # 设置重试次数
    retry = 1
    url = Config.callcenterUrl

    @screenshot
    @skip
    def test_call_center_Login(self):
        """呼叫中心登录验证"""
        main = Index(self.driver)
        main.common_Login("gzm", "Cango1234")
        main.callCenter_login()
        time.sleep(1)
        self.driver.send(Location("输入申请编号", "input", "css"), "BPA0792002002787")
        self.driver.click(Location("点击查询", 'div.button', "css"))


if __name__ == "__main__":
    unittest.main()
