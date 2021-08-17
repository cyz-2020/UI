from util.decorator import Log
from util.driver import ChromeDriver
from util.logger import Logger
from config import Config


class Login(object):
    logger = Logger().logger
    driver = None

    def __init__(self):
        # 启动driver 车务登录的初始化验证
        try:
            self.driver = ChromeDriver()
            self.driver.maximize_window()
            self.driver.get(Config.ccsUrl)
            self.driver.set_page_load_timeout(Config.TIMEOUT)
            self.driver.set_script_timeout(10)
        except Exception as e:
            Log.error("driver初始化失败....\n系统信息: {} \n浏览器类型: {}\n详细信息: {}".format(
                Config.system, Config.BROWSER, str(e)))
            if self.driver:
                self.driver.quit()
            raise Exception(e)

    def login(self):
        # 屏蔽登录部分
        # self.driver.send(self.username, Config.USER)
        # self.driver.send(self.passwd, Config.PWD)
        # self.driver.click(self.submit)
        # assert self.driver.exists(self.logo), "登录失败, 未找到大后台左上角logo"
        # assert self.driver.title == "微软 Bing 搜索 - 国内版", \
        #     "打开bing失败, 浏览器title不为'微软 Bing 搜索 - 国内版'，可能未进入bing首页"
        return self.driver


