import os
import subprocess
import getxmlimg
# 判断程序以正确方式运行
class ROOT:
    def GetRoot():
        return os.geteuid() == 0

class APK:
    def __init__(self, apkPath):
        self.apkPath = apkPath

    def install(self):
        os.system("pkexec /usr/bin/uengine-session-launch-helper -- uengine install --apk='{}'".format(self.apkPath))

    def information(self):
        return subprocess.getoutput("aapt dump badging '{}'".format(self.apkPath))

if __name__ == "__main__":
    print("本 API 不支持直接运行，请通过引入的方式使用此 API")
    quit()
if not ROOT.GetRoot():
    print("请获取 ROOT 权限以便更好的使用该 API")