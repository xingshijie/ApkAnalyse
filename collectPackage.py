import queue
import subprocess
import os
import threading
import json
import apkData
from pathlib import Path
from packageData import PackageData
from packageData import MyEncode

# 包名提取规则
# 1.在PackageName文件下
# 2.不是META-INF,android,assets,res文件下
# 3.逻辑:
#     1.轮训主目录下的所有文件,去除上面规定的特殊文件夹,假如文件夹名为dir_name
#     2.如果dir下有文件,则dir则是包名,退出此文件
#     3.如果没有文件,则继续往下找文件,继续2


def get_package(par_path, package_path, packages, depth):
    if depth > 4:
        return
    depth += 1
    package = package_path.replace('/', '.')
    packages.append(package)

    rel_path = Path(par_path + '/' + package_path)
    for d in rel_path.iterdir():
        if d.is_dir():
            get_package(par_path, package_path + '/' + d.name, packages, depth)
    # if len(list(rel_path.glob('*.class'))) > 0:
    #     package = package_path.replace('/', '.')
    #     packages.append(package)
    # else:
    #     for d in rel_path.iterdir():
    #         if d.is_dir():
    #             get_package(par_path, package_path + '/' + d.name, packages, depth)


apk_data_list = json.load(open('apk_data_list.json', 'r'), object_hook=apkData.as_payload)
apk_package_list = []

for apk_data in apk_data_list:
    path = 'apk/' + apk_data.package_name
    package_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            if f in ['META-INF', 'android', 'assets', 'res']:
                pass
            else:
                path2 = path + '/' + f
                if os.path.isdir(path2):
                    get_package(path, f, package_list, 1)
    else:
        print(path + 'is not existing')

    package_data = PackageData()
    package_data.name = apk_data.app_name
    package_data.package_name = apk_data.package_name
    package_data.lib_list = package_list
    apk_package_list.append(package_data)

fp = open('apk_package_list_4.json', 'w')
json.dump(apk_package_list, fp, ensure_ascii=False, cls=MyEncode)
