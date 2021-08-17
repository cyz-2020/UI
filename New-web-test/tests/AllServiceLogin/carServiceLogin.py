import logging
import unittest
from unittest import skip

from page.base import Location
from page.index import Index

from tests.base_case_class import BaseCaseCls
from util.decorator import screenshot
from util.logger import Logger

Log = Logger().logger


class CarServiceLogin(BaseCaseCls):
    # 设置重试次数
    retry = 1

    @screenshot
    @skip
    def test_car_service_Login(self):
        """车务服务登录验证"""
        main = Index(self.driver)
        main.common_Login("cyz114", "123456")
        main.carService_login()
        self.driver.click(Location("菜单是否存在", 'div.el-submenu__title', 'css'))
        Log.info(f'车务系统{self.driver.title}')
        # 断言
        # self.assertEqual("(ut)车务管理系统", self.driver.title,
        #                  "车务系统登录正常")


if __name__ == "__main__":
    unittest.main()
