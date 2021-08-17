from util.decorator import Log
from util.driver import ChromeDriver
from util.logger import Logger
from config import Config


class Login(object):
    logger = Logger().logger
    driver = None
    # username = Location("用户名输入框", "input[type=text]")
    # passwd = Location("密码输入框", "input[type=password]")
    # submit = Location("登录按钮", ".btn-login")
    # logo = Location("大后台管理系统图标", "#leftpanel .img")

    def __init__(self):
        # 启动driver 车务登录的初始化验证
        try:
            self.driver = ChromeDriver()
            self.driver.maximize_window()
            self.driver.get(Config.carserviceUrl)
            self.driver.set_page_load_timeout(Config.TIMEOUT)
            self.driver.set_script_timeout(10)
        except Exception as e:
            Log.error("driver初始化失败....\n系统信息: {} \n浏览器类型: {}\n详细信息: {}".format(
                Config.system, Config.BROWSER, str(e)))
            if self.driver:
                self.driver.quit()
            raise Exception(e)

    def login(self):
        return self.driver



