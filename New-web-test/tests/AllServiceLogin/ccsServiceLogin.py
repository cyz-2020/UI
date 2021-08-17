import logging
import time
import unittest
from unittest import skip

from page.base import Location
from page.index import Index
from tests.base_case_ccs import BaseCaseCCS
from util.decorator import screenshot
from util.logger import Logger

Log = Logger().logger


class CCSLogin(BaseCaseCCS):
    # 设置重试次数
    retry = 1

    @screenshot
    def test_ccs_service_Login(self):
        """CCS服务登录验证"""
        main = Index(self.driver)
        main.ccs_login()
        # self.driver.find_element_by_xpath("//*[@id='searchForm']/div[2]/div/a[1]").click()
        # title_path = Location("点击菜单", 'span.title', 'css')
        # ccs_title = Location("点击菜单", "//span[text()='电话催收']", 'xpath')
        # self.driver.click(title_path)
        Log.info(f'贷后催收系统{self.driver.title}')
        # 断言
        # self.assertEqual("(ut)车务管理系统", self.driver.title,
        #                  "CCS系统登录正常")


if __name__ == "__main__":
    unittest.main()
