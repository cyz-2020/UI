import importlib
import os
from typing import Any

from config import Config
from result.suite import Suite
from util.web_tool import Tools


def get_case():
    case_dir = {}
    suite = Config.suite_dir
    for root, dirs, files in os.walk(suite):
        # if root not in [os.path.join(suite, x) for x in Config.skip_suite]:
        for file in sorted(files):
            if not file.endswith(".pyc") and not file.startswith("base_case") \
                    and file.endswith(".py"):
                file = file.split(".")[0]
                suite_name = root.replace("\\", "/").split("/")[-1]  # 兼容/和\
                case_dir.update({suite_name: file})
                # print(case_dir)
    return case_dir


def get_case_cls(module, file, cls_name):
    for c in cls_name:
        _class = getattr(module, c)
        if _class.__name__ != "Base_Case":
            return _class, _class.__name__
    else:
        raise Exception("{}文件中未找到测试类!".format(file))


def create_suite():
    # get_xmind_case()  # 生成Xmind
    suite = Suite()
    all_case = get_case()
    # print(all_case)
    case_info = {}
    for k, v in all_case.items():
        # print(k, v)
        ss = "{}.{}.{}".format(Config.suite_name, k, v)
        # print(ss)
        cls_name = importlib.import_module(ss)
        # print(cls_name)
        # print(dir(cls_name))
        case,case_cls = Tools.get_case_cls(cls_name,k,dir(cls_name))



# get_case()
create_suite()
