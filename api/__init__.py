import os
import shutil
import zipfile
import traceback
import subprocess
from getxmlimg import getsavexml

class ProgramInformation:
    programPath = os.path.split(os.path.realpath(__file__))[0]  # 返回 string
    version = "1.6.0Alpha1"
    updateTime = "2022年05月15日"
    websize = ["https://gitee.com/gfdgd-xi/uengine-runner", "https://github.com/gfdgd-xi/uengine-runner"]
    home = os.path.expanduser('~')

# 判断程序以正确方式运行
class Check:
    def CheckDepend():
        depend = ["/usr/bin/uengine", "UEngine", "/usr/bin/adb", "adb", "/usr/bin/uengine-session-launch-helper", "UEngine", "/usr/bin/aapt", "aapt"]
        for i in range(0, len(depend), 2):
            if not os.path.exists(depend[i]):
                print("依赖{}不存在".format(depend[i + 1]))

class ROOT:
    def GetRoot():
        return os.geteuid() == 0

class APK:
    def __init__(self, apkPath):
        self.apkPath = apkPath

    def install(self):
        os.system("pkexec /usr/bin/uengine-session-launch-helper -- uengine install --apk='{}'".format(self.apkPath))

    def uninstall(self):
        os.system("pkexec /usr/bin/uengine-session-launch-helper -- uengine uninstall --pkg='{}'".format(self.apkPath))

    def information(self):
        return subprocess.getoutput("aapt dump badging '{}'".format(self.apkPath))

    def activityName(self):
        info = self.information()
        for line in info.split('\n'):
            if "launchable-activity" in line:
                line = line[0: line.index("label='")]
                line = line.replace("launchable-activity: ", "")
                line = line.replace("'", "")
                line = line.replace(" ", "")
                line = line.replace("name=", "")
                line = line.replace("label=", "")
                line = line.replace("icon=", "")
                return line

    # 获取 apk 包名
    def packageName(self):
        info = self.information()
        for line in info.split('\n'):
            if "package:" in line:
                line = line[0: line.index("versionCode='")]
                line = line.replace("package:", "")
                line = line.replace("name=", "")
                line = line.replace("'", "")
                line = line.replace(" ", "")
                return line

    # 获取软件的中文名称
    def chineseLabel(self) -> "获取软件的中文名称":
        info = self.information()
        for line in info.split('\n'):
            if "application-label:" in line:
                line = line.replace("application-label:", "")
                line = line.replace("'", "")
                return line

    # 保存apk图标
    def saveApkIcon(self, iconSavePath) -> "保存 apk 文件的图标":
        try:
            if os.path.exists(iconSavePath):
                os.remove(iconSavePath)
            info = self.information()
            for line in info.split('\n'):
                if "application:" in line:
                    xmlpath = line.split(":")[-1].split()[-1].split("=")[-1].replace("'", "")
                    if xmlpath.endswith('.xml'):
                        xmlsave = getsavexml()
                        print(xmlpath)
                        xmlsave.savexml(self.apkPath, xmlpath, iconSavePath)
                        return
                    else:
                        zip = zipfile.ZipFile(self.apkPath)
                        iconData = zip.read(xmlpath)
                        with open(iconSavePath, 'w+b') as saveIconFile:
                            saveIconFile.write(iconData)
                            return
            print("None Icon! Show defult icon")
            shutil.copy(ProgramInformation.programPath + "/defult.png", iconSavePath)
        except:
            traceback.print_exc()
            print("Error, show defult icon")
            shutil.copy(ProgramInformation.programPath + "/defult.png", iconSavePath)

    def version(self):
        info = self.information()
        for line in info.split('\n'):
            if "package:" in line:
                if "compileSdkVersion='" in line:
                    line = line.replace(line[line.index("compileSdkVersion='"): -1], "")
                if "platform" in line:
                    line = line.replace(line[line.index("platform"): -1], "")
                line = line.replace(line[0: line.index("versionName='")], "")
                line = line.replace("versionName='", "")
                line = line.replace("'", "")
                line = line.replace(" ", "")
                return line
            
    def saveDesktopFile(self, desktopPath, iconPath):
        showName = self.chineseLabel()
        if showName == "" or showName == None:
            showName = "未知应用"
        self.saveApkIcon(iconPath)
        things = '''[Desktop Entry]
        Categories=app;
        Encoding=UTF-8
        Exec=uengine launch --action=android.intent.action.MAIN --package={} --component={}
        GenericName={}
        Icon={}
        MimeType=
        Name={}
        StartupWMClass={}
        Terminal=false
        Type=Application
        '''.format(self.packageName(), self.activityName(), showName, iconPath, showName, showName)
        File(desktopPath).write(things)

class UEngine:
    def RemoveUengineCheck():
        os.remove("/usr/share/uengine/uengine-check-runnable.sh")
    def CPUCheck():
        return subprocess.getoutput("uengine check-features")
    class Services:
        def Open():
            os.system("pkexec systemctl enable uengine-container uengine-session && systemctl start uengine-container uengine-session")
        def Close():
            os.system("pkexec systemctl disable uengine-container uengine-session")
        def Restart():
            os.system("pkexec systemctl restart uengine*")

    class InternetBridge:
        def Open():
            os.system("pkexec uengine-bridge.sh start")
        def Close():
            os.system("pkexec uengine-bridge.sh stop")
        def Restart():
            os.system("pkexec uengine-bridge.sh restart")
        def Reload():
            os.system("pkexec uengine-bridge.sh reload")
        def ForceReload():
            os.system("pkexec uengine-bridge.sh force-reload")

class Adb:
    class Service:
        def Open():
            os.system("adb start-server")
        def Close():
            os.system("adb kill-server")
        def Kill():
            os.system("killall adb")

class File:
    def __init__(self, filePath):
        self.filePath = filePath

    def read(self):
        f = open(self.filePath, "r")  # 设置文件对象
        str = f.read()  # 获取内容
        f.close()  # 关闭文本对象
        return str  # 返回结果

    def write(self, things) -> "写入文本文档":
        TxtDir = os.path.dirname(self.filePath)
        print(TxtDir)
        if not os.path.exists(TxtDir):
            os.makedirs(TxtDir, exist_ok=True)
        file = open(self.filePath, 'w', encoding='UTF-8')  # 设置文件对象
        file.write(things)  # 写入文本
        file.close()  # 关闭文本对象

if __name__ == "__main__":
    print("本 API 不支持直接运行，请通过引入的方式使用此 API")
    apki = APK("/home/gfdgd_xi/下载/com.mihoyo.cloudgames.ys_1.0.0_liqucn.com.apk")
    print(apki.packageName())
    quit()

if not ROOT.GetRoot():
    print("请获取 ROOT 权限以便更好的使用该 API")