#!/usr/bin/env python3
import os
import sys
import json
import shutil
import requests
import traceback

# 读取文本文档
def read_txt(path):
    f = open(path,"r") # 设置文件对象
    str = f.read() # 获取内容
    f.close() # 关闭文本对象
    return str # 返回结果

def GetPackageUpdateInformation():
    global setting
    global package
    for i in allJson['Program']:
        if i['Package'] == package:
            return i

try:
    setting = json.loads(read_txt("{}/setting.json".format(os.path.split(os.path.realpath(__file__))[0])))
except:
    traceback.print_exc()
    print("配置文件无法访问！")
package = setting['Package']
nowVersion = setting['Version']
try:
    jsons = requests.get(setting["Url"])
except:
    traceback.print_exc()
    print("服务器出现错误！")
    sys.exit(1)
allJson = json.loads(jsons.text)
updateInformation = GetPackageUpdateInformation()
name = updateInformation['Name']
newVersion = updateInformation['Version']
print("更新程序：{}".format(name))
print("最新版本：{}".format(newVersion))
print("目前版本：{}".format(nowVersion))
if nowVersion == newVersion:
    print("目前是最新版本，无需更新！")
    quit()
print("更新内容：")
print(updateInformation['New Things'])
choose = input("更新？[Y/N]")
if choose.upper() == "N":
    quit()
if os.path.exists("/tmp/update-console-{}".format(package)):
    shutil.rmtree("/tmp/update-console-{}".format(package))
os.mkdir("/tmp/update-console-{}".format(package))
if updateInformation["Linux App Url"][0] == None:
    print("没有可用包源")
    quit()
os.system("wget '{}' -P '/tmp/update-console-{}'".format(updateInformation["Linux App Url"][0], package))
os.system("sudo dpkg -i /tmp/update-console-{}/*".format(package))
os.system("sudo apt install -f -y")