import ddt

from config import Config
from util.driver import ChromeDriver
from page.base import Base, Location

from util.web_tool import Tools
import time


# @ddt
class Index(Base):

    def common_Login(self, name, pwd):
        # 适合车务/呼叫中心
        name_input = Location("输入用户名", 'input', "css")
        pwd_input = Location("输入密码", "//input[@type='password']", "xpath")
        self.driver.send(name_input, name)
        self.driver.send(pwd_input, pwd)

    def search_dragonball_super(self):
        self.driver.send(self.search_input, "龙珠超")
        # print(self.search)
        self.driver.click(self.search)
        self.carService_login()

    # @ddt.data("cyz")
    def tc_apply(self, name):
        self.driver.click(self.tcframe)
        self.driver.click(self.tellinfo)
        # self.driver.click(Config)
        print(f'my name is {name}')

    def carService_login(self):
        """车务登录"""
        button_click = Location("点击登录", 'button', "css")
        self.driver.click(button_click)

    def callCenter_login(self):
        button_click = Location("点击登录", 'button.btn', "css")
        self.driver.click(button_click)

    def ccs_login(self):
        pass


if __name__ == '__main__':
    driver = ChromeDriver()
    m = Index(driver)
    lc = m.search
    print(lc.file)
    print(m.search)
