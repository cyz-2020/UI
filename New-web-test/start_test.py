import importlib  # 动态导入模块
import os
import sys
import unittest
from datetime import datetime

from result.generator import generate
from result.text_test_result import result
from result.suite import Suite
from util.chrome import Browser
from util.utils import Utils
from util.web_tool import Tools
from util.xmind_reader import Xmind
from config import Config

sys.path.append(os.getcwd())


def create_suite():
    # get_xmind_case()  # 生成Xmind
    suite = Suite()
    all_case = Tools.get_all_case()
    # print(all_case)
    case_info = {}
    for k, v in all_case.items():
        cls_name = importlib.import_module("{}.{}.{}".format(Config.suite_name, v, k))
        case, case_name = Tools.get_case_cls(cls_name, v, dir(cls_name))
        print(case, case_name)
        case_info.update({case_name: v})  # 对应用例和套件
        case_list = Tools.get_case_name(case)
        for c in case_list:
            # print('c',c)
            # print('case(C)',case(c))
            suite.addTest(case(c))
    Config.case_info = case_info
    # print(case_info)
    print(suite)
    return suite


def write_report(html):
    # file = "report{}.html".format(datetime.strftime(datetime.now(), "%Y-%m-%d %H-%M-%S"))
    file = "{}report.html".format(Config.car_title)
    Utils.make_dir(Config.report_path)
    filename = os.path.join(Config.report_path, file)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)


def run():
    # Browser.set_browser()
    start = datetime.now()
    suite = create_suite()
    Config.CASE_NUM = len(getattr(suite, "_tests"))
    runner = unittest.TextTestRunner(resultclass=result)
    rt = runner.run(suite)
    html, info, rv = generate(rt, start)
    write_report(html)


if __name__ == "__main__":
    run()
