import os
import platform
import sys


class BaseConf(object):
    # 测试环境
    ENV = "dev"
    ENV = "UAT"

    # 系统类型
    if platform.system().lower() == "darwin":
        SYS = "mac"
    elif platform.system().lower() == "windows":
        SYS = "win"
    else:
        SYS = "linux"

    # MAC os
    chrome_app = r"/Applications/Google\ Chrome.app/Contents/MacOS/"  # mac os chrome安装地址

    # Win
    chrome_reg = r"SOFTWARE\Google\Chrome\BLBeacon"  # win chrome注册表地址

    # 系统名称配置
    car_title = ''
    ccs_title = '贷后催收'
    dh_title = '贷后运营'

    # 用例配置

    soft_name = "{}登录首页".format(car_title)

    BROWSER = "Chrome"  # 启动浏览器
    # 车务地址
    carserviceUrl = 'http://10.42.3.160/carService/login';
    # 呼叫中心
    callcenterUrl = 'http://callcenter.999haoche.com:8354/callcenter/index.html#/login'
    # 贷后催收
    ccsUrl = "http://10.42.0.155:8080/dhcs/anonlogin.do?pwd=13579&logincd=test14"

    url = "http://www.bing.com"  # 首页
    user_dic = {'TC': '29', 'TCAgent': '4'}
    ccs = 'http://10.42.0.155:8080/dhcs/anonlogin.do?pwd=13579&logincd=test{}'
    ccs_url = ccs.format(user_dic.get('TC'))
    system = platform.platform()  # 系统信息
    print(ccs_url)
    driver_url = "https://npm.taobao.org/mirrors/chromedriver/"

    TIMEOUT = 12  # 元素等待超时时间

    exists = 10  # 元素存在等待时间

    report_title = "{}自动化测试报告".format(car_title)  # 报告名字

    # 不执行的测试集
    skip_suite = []

    # 路径配置

    # CASE_NUM = None

    ROOT = os.path.dirname(os.path.abspath(__file__))

    report_path = os.path.join(ROOT, "report")  # 报告路径

    driver_dir = os.path.join(ROOT, "chromedriver")  # 驱动路径

    pic_dir = os.path.join(ROOT, "screenshot")  # 截图路径

    suite_name = "tests"

    suite_dir = os.path.join(ROOT, suite_name)  # 测试套件路径

    report_mod = os.path.join(ROOT, "templates", "report_template.html")

    xmind = os.path.join(ROOT, "xmind_data")

    LOG_DIR = os.path.join(ROOT, "logs")  # 日志地址

    LOGGER = "webdriver_test"  # 日志名

    # 失败重跑次数（全局）
    RETRY = 0

    # 定位方法映射
    location = dict(css="CSS_SELECTOR", id="ID", name="NAME", xpath="XPATH",
                    link_text="LINK_TEXT", partial_link_text="PARTIAL_LINK_TEXT",
                    tag_name="TAG_NAME", class_name="CLASS_NAME")

    # mongo数据库配置信息
    MONGO_HOST = "10.42.0.210" if ENV == "dev" else "192.168.1.xx"
    MONGO_PORT = "3306" if ENV == "dev" else "27027"
    MONGO_USER = "ccstest"
    MONGO_PWD = "ccstest12345"
    MONGO_DB = "newerp"

    # 催收mysql配置信息

    MYSQL_HOST = "10.42.0.210" if ENV == "dev" else "192.168.1.xx"
    MYSQL_PORT = "3306"
    MYSQL_USER = "ccstest"
    MYSQL_PWD = "ccstest12345"

    # xmind头文件配置
    xmind_head = ["from tests.base_case import BaseCase",
                  "from util.decorator import screenshot"]

    # 车务数据库
    carENV = "dev"
    car_Host = "10.42.1.43" if carENV == "dev" else "192.168.121.198"
    car_Port = "3306"
    car_User = "carservice_admin"
    car_Pwd = "yO0b78UYGBH"

    #邮箱配置
    mail_host = "smtp.163.com"
    mail_user = "abc@163.com"
    mail_pass = "123456"
    mail_port = "25"
    sender = "abc@163.com"
    receiver = "123456@qq.com/1254367@qq.com"
    subject = "Interface Test Report"
    content = "All interface test has been complited\nplease read the report file about the detile of result in the attachment."
    testuser = "Someone"
    on_off = "off"


class CarServiceConf(BaseConf):
    url = "http://tieba.baidu.com"  # 测试百度贴吧配置


def set_config():
    name = sys.argv[1] if len(sys.argv) >= 2 else "BaseConf"
    cls_config = {"BaseConf": BaseConf, "SearchConf": CarServiceConf}
    print(cls_config.get(name))

    return cls_config.get(name, BaseConf)


class Config(set_config()):
    pass


print(Config.carENV)
