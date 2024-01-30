#!/usr/bin/env python3
# 使用系统默认的 python3 运行
###########################################################################################
# 作者：gfdgd xi<3025613752@qq.com>
# 版本：2.0.0
# 更新时间：2022年07月25日
# 感谢：anbox、deepin 和 UOS
# 基于 Python3 的 PyQt5 构建
# 更新：gfdgd xi<3025613752@qq.com>、actionchen<917981399@qq.com>
###########################################################################################
#################
# 引入所需的库
#################
import os
import api
import sys
import time
import json
import numpy
import base64
import socket
import shutil
import datetime
import zipfile
import platform
import requests
import traceback
import threading
import webbrowser
import subprocess
import updatekiller
map = True
import matplotlib
import matplotlib.figure
import matplotlib.pylab
import matplotlib.font_manager
import urllib.parse as parse
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
from getxmlimg import getsavexml
try:
    import PyQt5.QtWebEngineWidgets as QtWebEngineWidgets
    bad = False
except:
    bad = True
from Model import *

def PythonLower():
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QMessageBox.critical(None, "错误", "Python 至少需要 3.6 及以上版本，目前版本：" + platform.python_version() + "")
    sys.exit(1)

# Python 版本检测，因为 f-string 格式化要至少 Python 3.6 及以上的版本，所以需要检测
# 判断主版本号
if sys.version_info[0] < 3:
    PythonLower()
if sys.version_info[1] < 6:
    PythonLower()

print("""观沧海 曹操
东临碣石，以观沧海。水何澹澹，山岛竦峙。
树木丛生，百草丰茂。秋风萧瑟，洪波涌起。
日月之行，若出其中；星汉灿烂，若出其里。
幸甚至哉，歌以咏志。""")
print("")
print("""译文：东行登上碣石山，来观赏那苍茫的海。海水多么宽阔浩荡，山岛高高地挺立在海边。
树木和百草丛生，十分繁茂。秋风吹动树木发出悲凉的声音，海中涌着巨大的海浪。
太阳和月亮的运行，好像是从这浩瀚的海洋中发出的。银河星光灿烂，好像是从这浩瀚的海洋中产生出来的。
我很幸运，就用这首诗歌来表达自己内心的志向。""")
print("================================")

class UninstallProgram(QtCore.QThread):
    info = QtCore.pyqtSignal(str)
    error = QtCore.pyqtSignal(str)
    combo = QtCore.pyqtSignal(int)

    def __init__(self, package) -> None:
        self.package = package
        super().__init__()

    def run(self):
        package = self.package
        try:
            global fineUninstallApkHistory 
            Return = os.system("uengine uninstall --pkg='{}'".format(package))
            print(Return)
            if Return != 0:
                self.error.emit("疑似卸载失败，请检查 UEngine 是否正常安装、运行以及 APK 文件或包名是否正确、完整")
                DisabledAndEnbled(False)
                return
            if os.path.exists("{}/{}.desktop".format(desktopFilePath, package)):
                os.remove("{}/{}.desktop".format(desktopFilePath, package))
            if os.path.exists("{}/{}.desktop".format(get_desktop_path(), package)):
                os.remove("{}/{}.desktop".format(get_desktop_path(), package))
            findApkHistory.append(ComboInstallPath.currentText())
            self.combo.emit(0)
            write_txt(get_home() + "/.config/uengine-runner/FindApkHistory.json", str(json.dumps(ListToDictionary(findApkHistory))))  # 将历史记录的数组转换为字典并写入
            self.info.emit("操作执行完毕！")
            DisabledAndEnbled(False)
        except:
            traceback.print_exc()
            self.error.emit(traceback.format_exc())
            DisabledAndEnbled(False)
# 卸载程序
#def UninstallProgram(package: "apk 包名")->"卸载程序":
#    pass

# 卸载按钮事件
def ButtonClick8():
    if ComboInstallPath.currentText() is "":
        QtWidgets.QMessageBox.information(widget, "提示", langFile[lang]["Main"]["MainWindow"]["Error"]["UninstallError"])
        return
    DisabledAndEnbled(True)
    if os.path.exists(ComboInstallPath.currentText()):
        path = GetApkPackageName(ComboInstallPath.currentText())
    else:
        path = ComboInstallPath.currentText()
    print(path)
    QT.installRun = UninstallProgram(path)
    QT.installRun.error.connect(ErrorBox)
    QT.installRun.info.connect(InformationBox)
    QT.installRun.combo.connect(UpdateCombobox)
    QT.installRun.start()
    #threading.Thread(target=UninstallProgram, args=[path]).start()

# 浏览窗口
temppath=""
def FindApk()->"浏览窗口":
    path = QtWidgets.QFileDialog.getOpenFileName(widget, "选择 Apk", json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApk.json"))["path"], "APK 文件(*.apk);;所有文件(*.*)")[0]
    global temppath    
    temppath = path
    print("apk path is find:" + path)
    if path != "" and path != "()":
        try:
            ComboInstallPath.setEditText(path)
            write_txt(get_home() + "/.config/uengine-runner/FindApk.json", json.dumps({"path": os.path.dirname(path)}))  # 写入配置文件
        except:
            pass

class QT:
    installRun = None

# 安装按钮事件
def Button3Install():
    if ComboInstallPath.currentText() is "" or not os.path.exists(ComboInstallPath.currentText()):
        QtWidgets.QMessageBox.information(widget, "提示", langFile[lang]["Main"]["MainWindow"]["Error"]["InstallError"])
        return
    DisabledAndEnbled(True)
    #threading.Thread(target=InstallApk, args=(ComboInstallPath.get(),)).start()
    QT.installRun = InstallApk(ComboInstallPath.currentText())
    QT.installRun.infor.connect(InformationBox)
    QT.installRun.error.connect(ErrorBox)
    QT.installRun.combo.connect(UpdateCombobox)
    QT.installRun.make.connect(InstallBuildDesktop)
    QT.installRun.start()

# 安装应用
class InstallApk(QtCore.QThread):
    infor = QtCore.pyqtSignal(str)
    error = QtCore.pyqtSignal(str)
    combo = QtCore.pyqtSignal(int)
    make = QtCore.pyqtSignal(str)

    def __init__(self, path, quit = False) -> None:
        self.path = path
        self.quit = quit
        super().__init__()

    def run(self):
        path = self.path
        quit = self.quit
        # 将会强制改为拷贝安装，安装拷贝后的APK
        try:
            if not os.path.exists("/tmp/uengine-runner"):
                os.makedirs("/tmp/uengine-runner")
            if not os.path.exists(desktopFilePath):
                print("Mkdir")
                os.makedirs(desktopFilePath)
            # 读取设置
            setting = json.loads(readtxt(get_home() + "/.config/uengine-runner/setting.json"))
            # 安装应用
            print("start install apk")
            global findApkHistory
            print("start install apk12")
            iconSavePath = "{}/.local/share/icons/hicolor/256x256/apps/{}.png".format(get_home(), GetApkPackageName(path))
            tempstr1 = iconSavePath
            print("start install apk1")
            iconSaveDir = os.path.dirname(iconSavePath)
            if not os.path.exists(iconSaveDir):
                os.makedirs(iconSaveDir,exist_ok=True)
            SaveApkIcon(path, iconSavePath)
            try:
                shutil.copy(path, "/tmp/uengine-runner/bak.apk")
            except:
                QtWidgets.QMessageBox.critical(widget, "错误", "无法备份安装包，无法继续安装！")
                DisabledAndEnbled(False)
                return
            print(f"uengine install --apk='/tmp/uengine-runner/bak.apk'")
            commandReturn = os.system(f"uengine install --apk='/tmp/uengine-runner/bak.apk'")
            # 因为安装的是备份包，所以不需要再拷贝回去了（应该也没了）
            #try:
            #    if setting["SaveApk"]:
            #        shutil.copy("/tmp/uengine-runner/bak.apk", path)
            #except:
            #    self.error.emit(langFile[lang]["Main"]["MainWindow"]["Error"]["BackApkError"])
            if commandReturn != 0:
                self.error.emit("疑似 APK 安装失败，请检查 UEngine 是否正常安装、运行以及 APK 文件是否正确、完整")
                DisabledAndEnbled(False)
                return
            if settingConf["AutoScreenConfig"]:
                # 计算最合适的大小
                # 竖屏
                screen = QtGui.QGuiApplication.primaryScreen()
                mm = screen.availableGeometry()
                verticalHeighe = int(mm.height() * 0.9)                 # 竖屏高
                verticalWidth = int(verticalHeighe / 16 * 9)            # 竖屏宽
                horizontaltWidth = int(mm.width() * 0.8)                # 横屏宽
                horizontaltHeighe = int(horizontaltWidth / 16 * 9)      # 横屏高
                
                #verticalHeighe =
                write_txt(f"/tmp/{GetApkPackageName(path)}.txt", f"""verticalWidth {verticalWidth}  //竖屏宽
verticalHeighe {verticalHeighe} //竖屏高
horizontaltWidth {horizontaltWidth} //横屏宽，备选为1280
horizontaltHeighe {horizontaltHeighe} //横屏高 ，备选为720
verticalScreen  1 //设置默认横屏还是竖屏，1为竖屏，0为横屏   
allowFullScreen 1 //设置是否允许全屏，1为允许，0为不允许   
allowScreenSwitching 1 //设置是否允许横竖屏切换，1为允许，0为不允许  
defaultFullScreen 0 //设置是否默认显示最大化，1为默认最大化，0为不是 

logicalDensityDpi 160
physicalDpi 72
appWidth {verticalWidth}
appHeight {verticalHeighe}
logicalWidth {verticalWidth}
logicalHeight {verticalHeighe}
""")
                if os.system(f"pkexec '{programPath}/uengine-window-size-setting.py' -a {GetApkPackageName(path)}"):
                    self.error.emit("屏幕配置设置失败")
                    DisabledAndEnbled(False)
                    return
            if settingConf["ChooseProgramType"]:
                self.make.emit(iconSavePath)
            else:
                BuildUengineDesktop(GetApkPackageName(path), GetApkActivityName(path), GetApkChineseLabel(path), iconSavePath,
                            "{}/{}.desktop".format(get_desktop_path(), GetApkPackageName(path)))
                print("start install apk3")
                BuildUengineDesktop(GetApkPackageName(path), GetApkActivityName(path), GetApkChineseLabel(path), iconSavePath,
                           "{}/{}.desktop".format(desktopFilePath, GetApkPackageName(path)))
                print("\nprint install complete")
            if quit:
                return
            findApkHistory.append(ComboInstallPath.currentText())
            self.combo.emit(0)
            write_txt(get_home() + "/.config/uengine-runner/FindApkHistory.json", str(json.dumps(ListToDictionary(findApkHistory))))  # 将历史记录的数组转换为字典并写入
            self.infor.emit("操作完成！")
        except:
            traceback.print_exc()
            self.error.emit(traceback.format_exc())
        DisabledAndEnbled(False)

def InstallBuildDesktop(iconSavePath):
    choose = QtWidgets.QInputDialog.getItem(widget, "提示", "请选择分类，如果点击取消，将会设置为默认的分类", ["Network", "Chat", "Audio", "Video", "Graphics", "Office", "Translation", "Development", "Utility"])[0]
    path = ComboInstallPath.currentText()
    BuildUengineDesktop(GetApkPackageName(path), GetApkActivityName(path), GetApkChineseLabel(path), iconSavePath,
                            "{}/{}.desktop".format(get_desktop_path(), GetApkPackageName(path)), choose)
    print("start install apk3")
    BuildUengineDesktop(GetApkPackageName(path), GetApkActivityName(path), GetApkChineseLabel(path), iconSavePath,
                           "{}/{}.desktop".format(desktopFilePath, GetApkPackageName(path)), choose)
    print("\nprint install complete")

def UpdateCombobox(tmp):
    ComboInstallPath.clear()
    ComboInstallPath.addItems(findApkHistory)
    ComboInstallPath.setEditText(findApkHistory[-1])

def ErrorBox(error):
    QtWidgets.QMessageBox.critical(widget, "错误", error)

def InformationBox(info):
    QtWidgets.QMessageBox.information(widget, "提示", info)

# 禁用或启动所有控件
def DisabledAndEnbled(choose: "启动或者禁用")->"禁用或启动所有控件":
    ComboInstallPath.setDisabled(choose)
    #ComboUninstallPath.configure(state=a)
    BtnFindApk.setDisabled(choose)
    BtnInstall.setDisabled(choose)
    BtnAppStore.setDisabled(choose)
    BtnShowUengineApp.setDisabled(choose)
    #BtnUninstallApkBrowser.configure(state=a)
    BtnUninstall.setDisabled(choose)
    Btngeticon.setDisabled(choose)
    BtnSaveApk.setDisabled(choose)
    BtnApkInformation.setDisabled(choose)
    LabApkPath.setDisabled(choose)

# 需引入 subprocess
# 运行系统命令并获取返回值
def GetCommandReturn(cmd: "命令")->"运行系统命令并获取返回值":
    # cmd 是要获取输出的命令
    return subprocess.getoutput(cmd)

def GetSystemVersion():
    systemInformation = readtxt("/etc/os-release")
    for systemInformation in systemInformation.split('\n'):
        if "PRETTY_NAME=" in systemInformation:
            return systemInformation.replace("PRETTY_NAME=", "").replace('"', '')

# 打开所有窗口事件
def Button5Click():
    threading.Thread(target=OpenUengineProgramList).start()

# 打开“uengine 所有程序列表”
def OpenUengineProgramList()->"打开“uengine 所有程序列表”":
    os.system("uengine launch --package=org.anbox.appmgr --component=org.anbox.appmgr.AppViewActivity")

# 打开程序官网
def OpenProgramURL()->"打开程序官网":
    webbrowser.open_new_tab(programUrl)

# 重启本应用程序
def ReStartProgram()->"重启本应用程序":
    python = sys.executable
    os.execl(python, python, * sys.argv)

# 清理历史记录
def CleanProgramHistory()->"清理历史记录":
    try:
        if QtWidgets.QMessageBox.warning(widget, "警告", "删除后将无法恢复，你确定吗？\n删除后软件将会自动重启。", QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel) == QtWidgets.QMessageBox.Ok:
            shutil.rmtree(get_home() + "/.config/uengine-runner")
            ReStartProgram()
    except:
        traceback.print_exc()
        QtWidgets.QMessageBox.critical(widget, "错误", traceback.format_exc())

# 获取用户主目录
def get_home()->"获取用户主目录":
    return os.path.expanduser('~')

# 获取当前语言
def get_now_lang()->"获取当前语言":
    return os.getenv('LANG')

# 发送“启动 uengine 所有程序”的 .desktop 文件到桌面
def SendUengineAndroidListForDesktop()->"发送“启动 uengine 所有程序”的 .desktop 文件到桌面":
    global desktop
    global desktopName
    DisabledAndEnbled(True)
    try:
        if os.path.exists("{}/{}".format(get_desktop_path(), desktopName)):
            if QtWidgets.QMessageBox.question(widget, "提示", "桌面已经存在快捷方式，你确定要覆盖吗？") == QtWidgets.QMessageBox.No:
                DisabledAndEnbled(False)
                return
        shutil.copy(desktop, get_desktop_path())
        QtWidgets.QMessageBox.critical(widget, "提示", "发送成功！")
    except:
        traceback.print_exc()
        QtWidgets.QMessageBox.critical(widget, "错误", traceback.format_exc())
    DisabledAndEnbled(False)

# 获取用户桌面目录
def get_desktop_path()->"获取用户桌面目录":
    for line in open(get_home() + "/.config/user-dirs.dirs"):  # 以行来读取配置文件
        desktop_index = line.find("XDG_DESKTOP_DIR=\"")  # 寻找是否有对应项，有返回 0，没有返回 -1
        if desktop_index != -1:  # 如果有对应项
            break  # 结束循环
    if desktop_index == -1:  # 如果是提前结束，值一定≠-1，如果是没有提前结束，值一定＝-1
        return -1
    else:
        get = line[17:-2]  # 截取桌面目录路径
        get_index = get.find("$HOME")  # 寻找是否有对应的项，需要替换内容
        if get != -1:  # 如果有
            get = get.replace("$HOME", get_home())  # 则把其替换为用户目录（～）
        return get  # 返回目录

# 发送“启动 uengine 所有程序”的 .desktop 文件到启动器
def SendUengineAndroidListForLauncher()->"发送“启动 uengine 所有程序”的 .desktop 文件到启动器":
    DisabledAndEnbled(True)
    try:
        if os.path.exists("{}/.local/share/applications/{}".format(get_home(), desktopName)):
            if QtWidgets.QMessageBox.question(widget, "提示", "启动器已经存在快捷方式，你确定要覆盖吗？") == QtWidgets.QMessageBox.No:
                DisabledAndEnbled(False)
                return
        if not os.path.exists("{}/.local/share/applications/".format(get_home())):
            os.makedirs("{}/.local/share/applications/".format(get_home()))
        shutil.copy(desktop, "{}/.local/share/applications/{}".format(get_home(), desktopName))
        os.system("chmod 755 {}/.local/share/applications/{}".format(get_home(), desktopName))
        QtWidgets.QMessageBox.critical(widget, "提示", "发送成功！")
    except:
        traceback.print_exc()
        QtWidgets.QMessageBox.critical(widget, "错误", traceback.format_exc())
    DisabledAndEnbled(False)

# 数组转字典
def ListToDictionary(list: "需要转换的数组")->"数组转字典":
    dictionary = {}
    for i in range(len(list)):
        dictionary[i] = list[i]
    return dictionary

# 读取文本文档
def readtxt(path: "路径")->"读取文本文档":
    f = open(path, "r")  # 设置文件对象
    str = f.read()  # 获取内容
    f.close()  # 关闭文本对象
    return str  # 返回结果

# 写入文本文档
def write_txt(path: "路径", things: "内容")->"写入文本文档":
    TxtDir = os.path.dirname(path)
    print(TxtDir)
    if not os.path.exists(TxtDir):
        os.makedirs(TxtDir,exist_ok=True)    
    file = open(path, 'w', encoding='UTF-8')  # 设置文件对象
    file.write(things)  # 写入文本
    file.close()  # 关闭文本对象

# 获取 aapt 的所有信息
def GetApkInformation(apkFilePath: "apk 所在路径")->"获取 aapt 的所有信息":
    return GetCommandReturn("'{}/aapt/run-aapt.sh' dump badging '{}'".format(programPath, apkFilePath))

# 获取 apk Activity
def GetApkActivityName(apkFilePath: "apk 所在路径")->"获取 apk Activity":
    info = GetApkInformation(apkFilePath)
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
    return f"{GetApkPackageName(apkFilePath)}.Main"

# 获取 apk 包名
def GetApkPackageName(apkFilePath: "apk 所在路径")->"获取 apk 包名":
    info = GetApkInformation(apkFilePath)
    for line in info.split('\n'):
        if "package:" in line:
            line = line[0: line.index("versionCode='")]
            line = line.replace("package:", "")
            line = line.replace("name=", "")
            line = line.replace("'", "")
            line = line.replace(" ", "")
            return line

'''
Bail修改：
将以下5个函数的deepin-terminal的"-C"参数改为"-e"，
解决了BuildRootUengineImage()函数未输入密码自动回车的bug
'''
def InstallRootUengineImage():
    if not os.path.exists:
        os.mkdir("/tmp/uengine-runner")
    write_txt("/tmp/uengine-runner/install.sh", "sudo dpkg -i /tmp/uengine-runner/u*.deb\nsudo apt install -f")
    #threading.Thread(target=os.system, args=[f"'{programPath}/launch.sh' deepin-terminal -e \"wget -P '/tmp/uengine-runner' 'https://hub.fastgit.xyz/gfdgd-xi/uengine-runner/releases/download/U1.2.15/uengine-android-image_1.2.15_amd64.deb' && pkexec bash '/tmp/uengine-runner/install.sh'\""]).start()
    threading.Thread(target=OpenTerminal, args=[f"wget -P '/tmp/uengine-runner' 'https://hub.fastgit.xyz/gfdgd-xi/uengine-runner/releases/download/U1.2.15/uengine-android-image_1.2.15_amd64.deb' && pkexec bash '/tmp/uengine-runner/install.sh'"]).start()


def UengineUbuntuInstall():
    threading.Thread(target=OpenTerminal, args=[f"bash '{programPath + '/uengine-installer'}'"]).start()

def UengineUbuntuInstallRoot():
    # 加 SuperSU 参数
    threading.Thread(target=OpenTerminal, args=[f"bash '{programPath + '/uengine-installer'}' SuperSU"]).start()

def UbuntuInstallUengine():
    threading.Thread(target=OpenTerminal, args=[f"bash '{programPath + '/uengine-installer'}'"]).start()

def BuildRootUengineImage():
    threading.Thread(target=OpenTerminal, args=[f"bash '{programPath}/root-uengine.sh'"]).start()
    
def ReinstallUengineImage():
    threading.Thread(target=OpenTerminal, args=[f"pkexec apt reinstall uengine-android-image -y"]).start()


# 生成 uengine 启动文件到桌面
def BuildUengineDesktop(packageName: "软件包名", activityName: "activity", showName: "显示名称", iconPath: "程序图标所在目录", savePath:".desktop 文件保存路径", choose="")->"生成 uengine 启动文件到桌面":
    if showName == "" or showName == None:
        showName = "未知应用"
    if choose != "":
        things = f'''[Desktop Entry]
Encoding=UTF-8
Exec=uengine launch --action=android.intent.action.MAIN --package={packageName} --component={activityName}
GenericName={showName}
Icon={iconPath}
MimeType=
Name={showName}
StartupWMClass={showName}
Categories={choose};
Terminal=false
Type=Application
'''
    else:
        things = f'''[Desktop Entry]
Categories=app;
Encoding=UTF-8
Exec=uengine launch --action=android.intent.action.MAIN --package={packageName} --component={activityName}
GenericName={showName}
Icon={iconPath}
MimeType=
Name={showName}
StartupWMClass={showName}
Terminal=false
Type=Application
'''
    write_txt(savePath, things)

# 获取软件的中文名称
def GetApkChineseLabel(apkFilePath)->"获取软件的中文名称":
    info = GetApkInformation(apkFilePath)
    name = None
    for line in info.split('\n'):
        if "application-label-zh:" in line:
            line = line.replace("application-label-zh:", "")
            line = line.replace("'", "")
            return line
        if "application-label:" in line:
            line = line.replace("application-label:", "")
            line = line.replace("'", "")
            name = line
    return name

# 保存apk图标
def SaveApkIcon(apkFilePath, iconSavePath)->"保存 apk 文件的图标":
    try:
        if os.path.exists(iconSavePath):
            os.remove(iconSavePath)
        info = GetApkInformation(apkFilePath)
        for line in info.split('\n'):
            if "application:" in line:
                xmlpath = line.split(":")[-1].split()[-1].split("=")[-1].replace("'","")  
                if xmlpath.endswith('.xml'):
                        xmlsave = getsavexml()
                        print(xmlpath)
                        xmlsave.savexml(apkFilePath,xmlpath,iconSavePath)
                        return
                else:
                    zip = zipfile.ZipFile(apkFilePath)
                    iconData = zip.read(xmlpath)
                    with open(iconSavePath, 'w+b') as saveIconFile:
                        saveIconFile.write(iconData)
                        return
        print("None Icon! Show defult icon")
        shutil.copy(programPath + "/defult.svg", iconSavePath)
    except:
        traceback.print_exc()
        print("Error, show defult icon")
        shutil.copy(programPath + "/defult.svg", iconSavePath)

def saveicon():
    global temppath
    global tempstr1
    iconSavePath = "{}/.local/share/icons/hicolor/256x256/apps/{}.png".format(get_home(), GetApkPackageName(temppath))
    print(iconSavePath+"iconpaths")
    SaveApkIcon(temppath, iconSavePath)

def KeyboardToMouse():
    threading.Thread(target=os.system, args=["pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY {}/uengine-keyboard".format(programPath)]).start()

# 用户自行保存
def SaveIconToOtherPath():
    apkPath = ComboInstallPath.currentText()
    if apkPath == "":
        QtWidgets.QMessageBox.critical(widget, "错误", langFile[lang]["Main"]["MainWindow"]["Error"]["ChooseApkError"])
        return
    path = QtWidgets.QFileDialog.getSaveFileName(widget, "保存图标", "icon.png", "PNG 图片(*.png);;所有文件(*.*)", json.loads(readtxt(get_home() + "/.config/uengine-runner/SaveApkIcon.json"))["path"])[0]
    if not path == "":
        try:
            SaveApkIcon(apkPath, path)
        except:
            traceback.print_exc()
            QtWidgets.QMessageBox.critical(widget, "错误", langFile[lang]["Main"]["MainWindow"]["Error"]["SaveApkIconError"])
            return
        write_txt(get_home() + "/.config/uengine-runner/SaveApkIcon.json", json.dumps({"path": os.path.dirname(path)}))  # 写入配置文件
        findApkHistory.append(ComboInstallPath.currentText())
        UpdateCombobox(0)
        write_txt(get_home() + "/.config/uengine-runner/FindApkHistory.json", str(json.dumps(ListToDictionary(findApkHistory))))  # 将历史记录的数组转换为字典并写入
        QtWidgets.QMessageBox.information(widget, "提示", "保存成功！")

# 清空 uengine 数据
def BackUengineClean()->"清空 uengine 数据":
    print("Choose")
    if QtWidgets.QMessageBox.warning(widget, "警告", "清空后数据将会完全丢失，确定要继续吗？", QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel) == QtWidgets.QMessageBox.Ok:
        DisabledAndEnbled(True)
        try:
            if os.path.exists(desktopFilePath):
                shutil.rmtree(desktopFilePath)
        except:
            traceback.print_exc()
            QtWidgets.QMessageBox.critical(widget, "错误", traceback.format_exc())
        OpenTerminal(f"pkexec rm -rfv /data/uengine")
        return
    print("Choose False")

# 启用 uengine 网络桥接
def UengineBridgeStart()->"启用 uengine 网络桥接":
    DisabledAndEnbled(True)
    os.system("pkexec uengine-bridge.sh start")
    DisabledAndEnbled(False)

# 关闭 uengine 网络桥接
def UengineBridgeStop()->"关闭 uengine 网络桥接":
    DisabledAndEnbled(True)
    os.system("pkexec uengine-bridge.sh stop")
    DisabledAndEnbled(False)

# 重启 uengine 网络桥接
def UengineBridgeRestart()->"重启 uengine 网络桥接":
    DisabledAndEnbled(True)
    os.system("pkexec uengine-bridge.sh restart")
    DisabledAndEnbled(False)

# 加载 uengine 网络桥接
def UengineBridgeReload()->"加载 uengine 网络桥接":
    DisabledAndEnbled(True)
    os.system("pkexec uengine-bridge.sh reload")
    DisabledAndEnbled(False)

# 强制加载 uengine 网络桥接
def UengineBridgeForceReload()->"强制加载 uengine 网络桥接":
    DisabledAndEnbled(True)
    os.system("pkexec uengine-bridge.sh force-reload")
    DisabledAndEnbled(False)

# 启用 uengine 服务
def StartUengine()->"启用 uengine 服务":
    DisabledAndEnbled(True)
    os.system("systemctl enable uengine-container uengine-session && systemctl start uengine-container uengine-session")
    DisabledAndEnbled(False)

# 关闭 uengine 服务
def StopUengine()->"关闭 uengine 服务":
    DisabledAndEnbled(True)
    os.system("systemctl disable uengine-container uengine-session")
    DisabledAndEnbled(False)

# 重启 uengine 服务
def UengineRestart()->"重启 uengine 服务":
    DisabledAndEnbled(True)
    os.system("systemctl restart uengine*")
    DisabledAndEnbled(False)

def ScrcpyConnectUengine():
    if os.path.exists("/snap/bin/scrcpy"):
        threading.Thread(target=os.system, args=["/snap/bin/scrcpy -s '192.168.250.2:5555'"]).start()
        return
    if QtWidgets.QMessageBox.question(widget, "提示", "你没有安装Scrcpy（指使用Snap安装），\n如果你使用了其他方法安装了Scrcpy，可以输入命令“scrcpy -s '192.168.250.2:5555'”，\n是否现在要使用Snap安装Scrcpy？") == QtWidgets.QMessageBox.Yes:
        if not os.path.exists("/tmp/uengine-runner"):
            os.makedirs("/tmp/uengine-runner")
        write_txt("/tmp/uengine-runner/InstallScrcpy.sh", '''#!/bin/bash
sudo apt install snapd -y
sudo snap refresh
sudo snap install scrcpy''')
        threading.Thread(target=OpenTerminal, args=[f"chmod 777 /tmp/uengine-runner/InstallScrcpy.sh -Rv && pkexec /tmp/uengine-runner/InstallScrcpy.sh"]).start()
        return

# 获取用户桌面目录
def get_desktop_path()->"获取用户桌面目录":
    for line in open(get_home() + "/.config/user-dirs.dirs"):  # 以行来读取配置文件
        desktop_index = line.find("XDG_DESKTOP_DIR=\"")  # 寻找是否有对应项，有返回 0，没有返回 -1
        if desktop_index != -1:  # 如果有对应项
            break  # 结束循环
    if desktop_index == -1:  # 如果是提前结束，值一定≠-1，如果是没有提前结束，值一定＝-1
        return -1
    else:
        get = line[17:-2]  # 截取桌面目录路径
        get_index = get.find("$HOME")  # 寻找是否有对应的项，需要替换内容
        if get != -1:  # 如果有
            get = get.replace("$HOME", get_home())  # 则把其替换为用户目录（～）
        return get  # 返回目录

# 提取已安装程序的apk
def SaveInstallUengineApp():
    while True:
        result = QtWidgets.QInputDialog.getText(widget, "输入 APK 包名", "请输入要获取的apk包名以便进行下一步操作")
        if result[1] == False:
            return
        result = result[0]
        if os.path.exists("/data/uengine/data/data/app/{}-1".format(result)):
            break
        QtWidgets.QMessageBox.critical(widget, "错误", langFile[lang]["Main"]["MainWindow"]["Error"]["PathError"])
    path = QtWidgets.QFileDialog.getSaveFileName(widget, "保存apk", "~", "APK 文件(*.apk);;所有文件(*.*)", json.loads(readtxt(get_home() + "/.config/uengine-runner/SaveApk.json"))["path"])[0]
    if path == "" or path == ():
        return
    try:
        shutil.copy("/data/uengine/data/data/app/{}-1/base.apk".format(result), path)
        write_txt(get_home() + "/.config/uengine-runner/SaveApk.json", json.dumps({"path": os.path.dirname(path)}))
        QtWidgets.QMessageBox.information(widget, "提示", "提取完成！")
    except:
        traceback.print_exc()
        QtWidgets.QMessageBox.critical(widget, "错误", traceback.format_exc())
    
def UengineCheckCpu():
    english = GetCommandReturn("uengine check-features")
    QtWidgets.QMessageBox.information(widget, "提示", english)

# 获取用户主目录
def get_home()->"获取用户主目录":
    return os.path.expanduser('~')

# 删除所有的 uengine 应用快捷方式
def CleanAllUengineDesktopLink():
    if QtWidgets.QMessageBox.question(widget, "提示", "你是否要删除所有的 UEngine 应用快捷方式？") == QtWidgets.QMessageBox.No:
        try:
            shutil.rmtree("{}/.local/share/applications/uengine".format(get_home()))
            os.makedirs("{}/.local/share/applications/uengine".format(get_home()))
            QtWidgets.QMessageBox.information(widget, "提示", "删除完毕！")
        except:
            traceback.print_exc()
            QtWidgets.QMessageBox.critical(widget, "错误", traceback.format_exc())

# 打开 uengine 应用打包器
def OpenUengineDebBuilder():
    threading.Thread(target=os.system, args=[f"'{programPath}/uengine-apk-builder' '{ComboInstallPath.currentText()}'"]).start()

# 打开 uengine 根目录
def OpenUengineRootData():
    threading.Thread(target=os.system, args=["xdg-open /data/uengine/data/data"]).start()

# 打开 uengine 用户数据目录
def OpenUengineUserData():
    threading.Thread(target=os.system, args=["xdg-open ~/安卓应用文件"]).start()

# 终端显示 adb 命令行
def AdbShellShowInTer():
    os.system("adb connect 192.168.250.2:5555")
    threading.Thread(target=OpenTerminal, args=[f"adb -s 192.168.250.2:5555 shell"]).start()

# 终端显示 adb top
def AdbCPUAndRAWShowInTer():
    os.system("adb connect 192.168.250.2:5555")
    threading.Thread(target=OpenTerminal, args=[f"adb -s 192.168.250.2:5555 shell top"]).start()

def UengineSettingShow():
    threading.Thread(target=os.system, args=["/usr/bin/uengine launch --action=android.intent.action.MAIN --package=com.android.settings --component=com.android.settings.Settings"]).start()

# 杀死 adb 进程
def AdbKillAdbProgress():
    os.system("killall adb")
    QtWidgets.QMessageBox.information(widget, "提示", "完成！")

# 关闭 adb 服务
def AdbStopServer():
    os.system("adb kill-server")
    QtWidgets.QMessageBox.information(widget, "提示", "完成！")

# 开启 adb 服务
def AdbStartServer():
    os.system("adb start-server")
    QtWidgets.QMessageBox.information(widget, "提示", "完成！")

def ReinstallUengine():
    threading.Thread(target=OpenTerminal, args=[f"pkexec apt reinstall uengine uengine-android-image uengine-modules-dkms -y && notify-send -i uengine \"安装完毕！\""]).start()

def DelUengineCheck():
    if not os.path.exists("/usr/share/uengine/uengine-check-runnable.sh"):
        QtWidgets.QMessageBox.information(widget, "提示", "本功能已经被删除，无法重复删除！")
        return
    if QtWidgets.QMessageBox.warning(widget, "警告", "删除后将无法使用本软件恢复\n如果需要恢复本功能，请重新安装 UEngine！", QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Ok) == QtWidgets.QMessageBox.Ok:
        threading.Thread(target=OpenTerminal, args=[f"pkexec rm -v /usr/share/uengine/uengine-check-runnable.sh"]).start()

# 使用 adb 连接 uengine
def UengineConnectAdb():
    QtWidgets.QMessageBox.information(widget, "提示", subprocess.getoutput("adb connect 192.168.250.2:5555"))

# 允许用户使用 adb
def UengineUseAdb():
    # 因为需要 root，所以需要开二号程序
    os.system("adb start-server")  # 保证有生成文件
    os.system("pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY {}/uengine-useadb 0 '{}'".format(programPath, "{}/.android/adbkey.pub".format(get_home())))  # 写入配置
    if QtWidgets.QMessageBox.question(widget, "提示", "是否要连接到 UEngine？") == QtWidgets.QMessageBox.Yes:
        UengineConnectAdb()

def UengineDoNotUseAdb():
    # 因为需要 root，所以需要开二号程序
    if not os.path.exists("/data/uengine/data/data/misc/adb/adb_keys"):
        QtWidgets.QMessageBox.critical(widget, "提示", "你的 uengine 在设置前已经禁用 adb 连接，无需重复设置")
        return
    threading.Thread(target=os.system, args=["pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY {}/uengine-useadb 1".format(programPath)]).start()

def UengineRunnerBugUpload():
    threading.Thread(target=os.system, args=[programPath + "/uengine-runner-update-bug"]).start()

def AdbConnectDeviceShow():
    ShowTextTipsWindow.ShowWindow(subprocess.getoutput("adb devices -l"))

def AdbAndroidInstallAppList():
    ShowTextTipsWindow.ShowWindow('''系统应用：
{}
第三方应用：
{}
全部应用以及apk所在路径：
{}'''.format(subprocess.getoutput("adb -s 192.168.250.2:5555 shell pm list packages -s"),
    subprocess.getoutput("adb -s 192.168.250.2:5555 shell pm list package -3"),
    subprocess.getoutput("adb -s 192.168.250.2:5555 shell pm list packages -f")))

def GetApkVersion(apkFilePath):
    info = GetApkInformation(apkFilePath)
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

def VersionCheck(version1, version2):
    return version1 == version2

def ShowHelp():
    global webHelp
    # 先判断是否能连接服务器，如果能则访问线上版本，否则访问本地的帮助文件
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.settimeout(1000)
    url = "file://" + programPath + "/Help/index.html"
    try:
        sk.connect(("uengine-runner.gfdgdxi.top", 80))
        url = f"http://uengine-runner.gfdgdxi.top"
    except:
        traceback.print_exc()
    if bad:
        # 如果没有安装 QWebEngine，则直接用浏览器打开
        webbrowser.open_new_tab(url)
        return
    # 否则用 QWebEngine 打开
    webHelp = QtWebEngineWidgets.QWebEngineView()
    webHelp.setWindowTitle("获取程序帮助")
    webHelp.setUrl(QtCore.QUrl(url))
    webHelp.setWindowIcon(QtGui.QIcon(iconPath))
    webHelp.resize(int(webHelp.frameGeometry().width() * 1.3), int(webHelp.frameGeometry().height() * 1.1))
    webHelp.show()

def AllowOrDisallowUpdateAndroidApp():
    if not os.path.exists("/data/uengine/data/data/misc/adb/adb_keys"):
        if QtWidgets.QMessageBox.question(widget, langFile[lang]["Main"]["MainWindow"]["Answer"]["Title"], langFile[lang]["Main"]["MainWindow"]["Answer"]["UseAdbPackageAnswer"]) == QtWidgets.QMessageBox.No:
            return
        os.system("pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY {}/uengine-useadb 0 '{}'".format(programPath,"{}/.android/adbkey.pub".format(get_home())))  # 写入配
    adb = api.Adb("192.168.250.2:5555")
    adb.Service.Close()
    adb.connect()
    if QtWidgets.QMessageBox.question(widget, langFile[lang]["Main"]["MainWindow"]["Answer"]["Title"], message=langFile[lang]["Main"]["MainWindow"]["Answer"]["AllowOrDisallowUpdateAndroidAppAnswer"][int(adb.boolAndroidInstallOtherAppSetting())]) == QtWidgets.QMessageBox.Yes:
        adb.setAndroidInstallOtherAppSetting(not adb.boolAndroidInstallOtherAppSetting())
        QtWidgets.QMessageBox.information(widget, langFile[lang]["Main"]["MainWindow"]["Information"]["Title"], langFile[lang]["Main"]["MainWindow"]["Answer"]["CompleteInformation"])

def SetHttpProxy():
    adb = api.Adb("192.168.250.2:5555")
    adb.Service.Close()
    adb.connect()
    if QtWidgets.QMessageBox.question(widget, "提示", "此功能需要安装 adb 补丁，请保证已经安装然后按下“Yes”") == QtWidgets.QMessageBox.No:
        return
    proxy = QtWidgets.QInputDialog.getText(widget, "输入代理", "请输入要设置的代理（为空代表不设置代理）")
    if proxy[1] == False:
        return
    if proxy[0] == "":
        os.system("adb -s 192.168.250.2:5555 shell settings delete global http_proxy")
        os.system("adb -s 192.168.250.2:5555 shell settings delete global global_http_proxy_host")
        os.system("adb -s 192.168.250.2:5555 shell settings delete global global_http_proxy_port")
        QtWidgets.QMessageBox.information(widget, "提示", "设置成功！")
    else:
        os.system(f"adb -s 192.168.250.2:5555 shell settings put global http_proxy \"{proxy[0]}\"")
        QtWidgets.QMessageBox.information(widget, "提示", "设置成功！")
    
class UengineWindowSizeSetting:
    setting = None
    package = "com.nuts.extremspeedup"
    verticalWidth = None
    verticalHeighe = None
    horizontaltWidth = None
    horizontaltHeighe = None
    verticalScreen = None
    allowFullScreen = None
    allowScreenSwitching = None
    defaultFullScreen = None
    logicalDensityDpi = None
    physicalDpi = None
    appWidth = None
    appHeight = None
    logicalWidth = None
    logicalHeight = None
    lineEdit = {
        "verticalWidth": verticalWidth,
        "verticalHeighe": verticalHeighe,
        "horizontaltWidth": horizontaltWidth,
        "horizontaltHeighe": horizontaltHeighe,
        "logicalDensityDpi": logicalDensityDpi,
        "physicalDpi": physicalDpi,
        "appWidth": appWidth,
        "appHeight": appHeight,
        "logicalWidth": logicalWidth,
        "logicalHeight": logicalHeight
    }
    checkbox = {
        "verticalScreen": verticalScreen,
        "allowFullScreen": allowFullScreen,
        "allowScreenSwitching": allowScreenSwitching,
        "defaultFullScreen": defaultFullScreen
    }
    def ShowWindow():
        unfound = False
        while True:
            if ComboInstallPath.currentText() == "":
                choose = QtWidgets.QInputDialog.getText(widget, "输入", "请输入需要设置的 Android 应用的包名")
            else:
                if GetApkPackageName(ComboInstallPath.currentText()) == None:
                    choose = QtWidgets.QInputDialog.getText(widget, "输入", "请输入需要设置的 Android 应用的包名", text=ComboInstallPath.currentText())
                else:
                    choose = QtWidgets.QInputDialog.getText(widget, "输入", "请输入需要设置的 Android 应用的包名", text=GetApkPackageName(ComboInstallPath.currentText()))
            if not choose[1]:
                return
            if choose[0] == "":
                QtWidgets.QMessageBox.information(widget, "提示", "包名不能为空")
                continue
            if not os.path.exists(f"/usr/share/uengine/appetc/{choose[0]}.txt"):
                if QtWidgets.QMessageBox.question(widget, "提示", "未找到这个包名对应的配置文件，是否要创建一个？") == QtWidgets.QMessageBox.No:
                    continue
                unfound = True
            UengineWindowSizeSetting.package = choose[0]
            break
        UengineWindowSizeSetting.setting = QtWidgets.QMainWindow()
        settingWidget = QtWidgets.QWidget()
        settingLayout = QtWidgets.QGridLayout()

        UengineWindowSizeSetting.verticalWidth = QtWidgets.QLineEdit()
        UengineWindowSizeSetting.verticalHeighe = QtWidgets.QLineEdit()
        UengineWindowSizeSetting.horizontaltWidth = QtWidgets.QLineEdit()
        UengineWindowSizeSetting.horizontaltHeighe = QtWidgets.QLineEdit()
        UengineWindowSizeSetting.verticalScreen = QtWidgets.QCheckBox("默认为竖屏")
        UengineWindowSizeSetting.allowFullScreen = QtWidgets.QCheckBox("允许全屏")
        UengineWindowSizeSetting.allowScreenSwitching = QtWidgets.QCheckBox("允许横竖屏切换")
        UengineWindowSizeSetting.defaultFullScreen = QtWidgets.QCheckBox("默认显示最大化")
        UengineWindowSizeSetting.logicalDensityDpi = QtWidgets.QLineEdit()
        UengineWindowSizeSetting.physicalDpi = QtWidgets.QLineEdit()
        UengineWindowSizeSetting.appWidth = QtWidgets.QLineEdit()
        UengineWindowSizeSetting.appHeight = QtWidgets.QLineEdit()
        UengineWindowSizeSetting.logicalWidth = QtWidgets.QLineEdit()
        UengineWindowSizeSetting.logicalHeight = QtWidgets.QLineEdit()
        saveButton = QtWidgets.QPushButton("保存设置")
        deleButton = QtWidgets.QPushButton("删除设置")
        saveButton.clicked.connect(UengineWindowSizeSetting.SaveSetting)
        deleButton.clicked.connect(UengineWindowSizeSetting.DeleteSetting)
        settingLayout.addWidget(QtWidgets.QLabel("竖屏宽："), 0, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.verticalWidth, 0, 1, 1, 2)
        settingLayout.addWidget(QtWidgets.QLabel("竖屏高："), 1, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.verticalHeighe, 1, 1, 1, 2)
        settingLayout.addWidget(QtWidgets.QLabel("横屏宽，备选为1280："), 2, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.horizontaltWidth, 2, 1, 1, 2)
        settingLayout.addWidget(QtWidgets.QLabel("横屏高，备选为720："), 3, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.horizontaltHeighe, 3, 1, 1, 2)
        settingLayout.addWidget(QtWidgets.QLabel("设置默认横屏还是竖屏："), 4, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.verticalScreen, 4, 1, 1, 2)
        settingLayout.addWidget(QtWidgets.QLabel("设置是否允许全屏："), 5, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.allowFullScreen, 5, 1, 1, 2)
        settingLayout.addWidget(QtWidgets.QLabel("设置是否允许横竖屏切换："), 6, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.allowScreenSwitching, 6, 1, 1, 2)
        settingLayout.addWidget(QtWidgets.QLabel("设置是否默认显示最大化："), 7, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.defaultFullScreen, 7, 1, 1, 2)
        settingLayout.addWidget(QtWidgets.QLabel("<hr>"), 8, 0, 1, 3)
        settingLayout.addWidget(QtWidgets.QLabel("屏幕缩放，数值大则大："), 9, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.logicalDensityDpi, 9, 1, 1, 2)
        settingLayout.addWidget(QtWidgets.QLabel("physicalDpi："), 10, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.physicalDpi, 10, 1, 1, 2)
        settingLayout.addWidget(QtWidgets.QLabel("appWidth："), 11, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.appWidth, 11, 1, 1, 2)
        settingLayout.addWidget(QtWidgets.QLabel("appHeight："), 12, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.appHeight, 12, 1, 1, 2)
        settingLayout.addWidget(QtWidgets.QLabel("logicalWidth："), 13, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.logicalWidth, 13, 1, 1, 2)
        settingLayout.addWidget(QtWidgets.QLabel("logicalHeight："), 14, 0, 1, 1)
        settingLayout.addWidget(UengineWindowSizeSetting.logicalHeight, 14, 1, 1, 2)
        settingLayout.addWidget(saveButton, 15, 1, 1, 1)
        settingLayout.addWidget(deleButton, 15, 2, 1, 1)
        UengineWindowSizeSetting.lineEdit = {
        "verticalWidth": UengineWindowSizeSetting.verticalWidth,
        "verticalHeighe": UengineWindowSizeSetting.verticalHeighe,
        "horizontaltWidth": UengineWindowSizeSetting.horizontaltWidth,
        "horizontaltHeighe": UengineWindowSizeSetting.horizontaltHeighe,
        "logicalDensityDpi": UengineWindowSizeSetting.logicalDensityDpi,
        "physicalDpi": UengineWindowSizeSetting.physicalDpi,
        "appWidth": UengineWindowSizeSetting.appWidth,
        "appHeight": UengineWindowSizeSetting.appHeight,
        "logicalWidth": UengineWindowSizeSetting.logicalWidth,
        "logicalHeight": UengineWindowSizeSetting.logicalHeight
    }
        UengineWindowSizeSetting.checkbox = {
        "verticalScreen": UengineWindowSizeSetting.verticalScreen,
        "allowFullScreen": UengineWindowSizeSetting.allowFullScreen,
        "allowScreenSwitching": UengineWindowSizeSetting.allowScreenSwitching,
        "defaultFullScreen": UengineWindowSizeSetting.defaultFullScreen
    }
        settingWidget.setLayout(settingLayout)
        UengineWindowSizeSetting.setting.setCentralWidget(settingWidget)
        if not unfound:
            UengineWindowSizeSetting.ReadSetting()
        else:
            for i in UengineWindowSizeSetting.checkbox.values():
                i.setChecked(True)
        UengineWindowSizeSetting.setting.setWindowTitle(f"设置 Android 应用的窗口大小缩放设置")
        UengineWindowSizeSetting.setting.show()
        UengineWindowSizeSetting.setting.resize(int(UengineWindowSizeSetting.setting.frameSize().width() * 1.3), int(UengineWindowSizeSetting.setting.frameSize().height()))

    def ReadSetting():
        file = open(f"/usr/share/uengine/appetc/{UengineWindowSizeSetting.package}.txt")
        while True:
            line = file.readline()
            if not line:
                break
            line = line.strip()
            print(line)
            if "//" in line:
                line = line[:line.index("//")]
            try:
                if line[:line.index(" ")].strip() in UengineWindowSizeSetting.lineEdit.keys():
                    UengineWindowSizeSetting.lineEdit[line[:line.index(" ")].strip()].setText(line[line.index(" "):].strip())
                if line[:line.index(" ")].strip() in UengineWindowSizeSetting.checkbox.keys():
                    UengineWindowSizeSetting.checkbox[line[:line.index(" ")].strip()].setChecked(bool(line[line.index(" "):].strip()))
            except:  # 错误行，忽略
                pass
        file.close()

    def SaveSetting():
        file = open(f"/tmp/{UengineWindowSizeSetting.package}.txt", "w")
        for i in UengineWindowSizeSetting.lineEdit.keys():
            if UengineWindowSizeSetting.lineEdit[i].text() == "":  # 空选项，不写入
                continue
            try:            
                file.write(f"{i} {int(UengineWindowSizeSetting.lineEdit[i].text())}\n")
            except:
                traceback.print_exc()
                QtWidgets.QMessageBox.critical(widget, "错误", "格式输入错误")
                return
        for i in UengineWindowSizeSetting.checkbox.keys():
            try:            
                file.write(f"{i} {int(UengineWindowSizeSetting.checkbox[i].isChecked())}\n")
            except:
                traceback.print_exc()
                QtWidgets.QMessageBox.critical(widget, "错误", traceback.format_exc())
                return
        file.close()
        if os.system(f"pkexec '{programPath}/uengine-window-size-setting.py' -a {UengineWindowSizeSetting.package}"):
            QtWidgets.QMessageBox.critical(widget, "错误", "保存失败")
            return
        QtWidgets.QMessageBox.information(widget, "提示", "保存完成！")

    def DeleteSetting():
        if os.system(f"pkexec '{programPath}/uengine-window-size-setting.py' -d {UengineWindowSizeSetting.package}"):
            QtWidgets.QMessageBox.critical(widget, "错误", "删除失败")
            return
        QtWidgets.QMessageBox.information(widget, "提示", "删除完成！")
        

class SettingWindow():
    saveApkOption = None
    settingWindow = None
    autoScreenConfig = None
    chooseProgramType = None
    theme = None
    def ShowWindow():
        SettingWindow.settingWindow = QtWidgets.QMainWindow()
        setting = QtWidgets.QWidget()
        settingLayout = QtWidgets.QGridLayout()

        SettingWindow.saveApkOption = QtWidgets.QComboBox()
        SettingWindow.autoScreenConfig = QtWidgets.QCheckBox("安装APK时自动根据系统分辨率设置，卸载时自动移除")
        SettingWindow.chooseProgramType = QtWidgets.QCheckBox("安装APK时手动选择程序分类")
        SettingWindow.theme = QtWidgets.QComboBox()
        themeTry = QtWidgets.QPushButton("测试(重启后变回设置的主题)")
        SettingWindow.theme.addItems(QtWidgets.QStyleFactory.keys())
        controlFrame = QtWidgets.QHBoxLayout()
        cancalButton = QtWidgets.QPushButton("取消")
        okButton = QtWidgets.QPushButton("保存")

        #settingLayout.addWidget(QtWidgets.QLabel("APK 安装模式："), 0, 0, 1, 1)
        #settingLayout.addWidget(SettingWindow.saveApkOption, 0, 1, 1, 1)
        settingLayout.addWidget(QtWidgets.QLabel("窗口大小策略："), 1, 0, 1, 1)
        settingLayout.addWidget(SettingWindow.autoScreenConfig, 1, 1, 1, 1)
        settingLayout.addWidget(QtWidgets.QLabel("程序分类策略："), 2, 0, 1, 1)
        settingLayout.addWidget(SettingWindow.chooseProgramType, 2, 1, 1, 1)
        settingLayout.addWidget(QtWidgets.QLabel("程序主题："), 3, 0, 1, 1)
        settingLayout.addWidget(SettingWindow.theme, 3, 1, 1, 1)
        settingLayout.addWidget(themeTry, 3, 2, 1, 1)
        settingLayout.addLayout(controlFrame, 4, 1, 1, 2)
        controlFrame.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        controlFrame.addWidget(cancalButton)
        controlFrame.addWidget(okButton)
        
        SettingWindow.saveApkOption.addItems(["不备份Apk包直接安装", "备份Apk包然后在安装后自动拷贝原先目录"])
        try:
            data = json.loads(readtxt(get_home() + "/.config/uengine-runner/setting.json"))
        except:
            QtWidgets.QMessageBox.critical(widget, "错误", langFile[lang]["Main"]["MainWindow"]["Error"]["SettingReadError"])
            SettingWindow.settingWindow.close()
            return
        SettingWindow.autoScreenConfig.setChecked(settingConf["AutoScreenConfig"])
        SettingWindow.saveApkOption.setCurrentIndex(int(data["SaveApk"]))
        SettingWindow.chooseProgramType.setChecked(settingConf["ChooseProgramType"])
        SettingWindow.theme.setCurrentText(settingConf["Theme"])
        themeTry.clicked.connect(SettingWindow.Try)
        cancalButton.clicked.connect(SettingWindow.settingWindow.close)
        okButton.clicked.connect(SettingWindow.SaveSetting)

        setting.setLayout(settingLayout)
        SettingWindow.settingWindow.setWindowTitle(f"设置 UEngine 运行器 {version}")
        SettingWindow.settingWindow.setWindowIcon(QtGui.QIcon(iconPath))
        SettingWindow.settingWindow.setCentralWidget(setting)
        SettingWindow.settingWindow.show()
        SettingWindow.settingWindow.setFixedSize(SettingWindow.settingWindow.frameSize().width(), SettingWindow.settingWindow.frameSize().height())
        
    def Try():
        app.setStyle(QtWidgets.QStyleFactory.create(SettingWindow.theme.currentText()))

    def SaveSetting():
        global settingConf
        try:
            write_txt(get_home() + "/.config/uengine-runner/setting.json", json.dumps({
                "SaveApk": bool(SettingWindow.saveApkOption.currentIndex()),
                "AutoScreenConfig": SettingWindow.autoScreenConfig.isChecked(),
                "ChooseProgramType": SettingWindow.chooseProgramType.isChecked(),
                "Theme": SettingWindow.theme.currentText()
                }))
            settingConf = {
                "SaveApk": bool(SettingWindow.saveApkOption.currentIndex()),
                "AutoScreenConfig": SettingWindow.autoScreenConfig.isChecked(),
                "ChooseProgramType": SettingWindow.chooseProgramType.isChecked(),
                "Theme": SettingWindow.theme.currentText()
                }
            app.setStyle(QtWidgets.QStyleFactory.create(SettingWindow.theme.currentText()))
        except:
            traceback.print_exc()
            QtWidgets.QMessageBox.critical(widget, "错误", langFile[lang]["Main"]["MainWindow"]["Error"]["SettingSaveError"])
            return
        QtWidgets.QMessageBox.information(widget, "提示", "设置保存完毕！")

class UpdateWindow():
    data = {}
    update = None
    def ShowWindow():
        UpdateWindow.update = QtWidgets.QMainWindow()
        updateWidget = QtWidgets.QWidget()
        updateWidgetLayout = QtWidgets.QGridLayout()
        versionLabel = QtWidgets.QLabel(f"当前版本：{version}\n最新版本：未知\n更新内容：")
        updateText = QtWidgets.QTextBrowser()
        ok = QtWidgets.QPushButton("更新（更新过程中会关闭这个应用的所有进程）")
        ok.clicked.connect(UpdateWindow.Update)
        cancel = QtWidgets.QPushButton("取消")
        cancel.clicked.connect(UpdateWindow.update.close)
        ok.setDisabled(True)
        try:
            UpdateWindow.data = json.loads(requests.get("http://update.gfdgdxi.top/uengine-runner/update.json").text)
            versionLabel = QtWidgets.QLabel(f"当前版本：{version}\n最新版本：{UpdateWindow.data['Version']}\n更新内容：")
            if UpdateWindow.data["Version"] == version:
                updateText.setText("此为最新版本，无需更新")
                ok.setDisabled(True)
            else:
                # 版本号读取（防止出现高版本号提示要“升级”到低版本号的问题）
                localVersionList = version.split(".")
                webVersionList = UpdateWindow.data['Version'].split(".")
                for i in range(len(localVersionList)):
                    local = int(localVersionList[i])
                    web = int(webVersionList[i])
                    if web < local:
                        updateText.setHtml(f"""<p>此为最新版本，无需更新，但似乎您当前使用的程序版本比云端版本还要高。</p>
<p>出现这个问题可能会有如下几种情况：</p>
<p>1、使用编译或者内测版本</p>
<p>2、自己修改了程序版本</p>
<p>3、作者忘记更新云端上的更新信息了</p>
<p>如果是第三种情况，请反馈到此：https://gitee.com/gfdgd-xi/uengine-runner/issues/I6B091</p>
<p><img src='{programPath}/Icon/doge.png'></p>""")
                        ok.setDisabled(True)
                        break
                    if web > local:
                        updateText.setText(UpdateWindow.data["New"].replace("\\n", "\n"))
                        ok.setEnabled(True)
                        break
                
        except:
            traceback.print_exc()
            QtWidgets.QMessageBox.critical(updateWidget, "错误", "无法连接服务器！")
        updateWidgetLayout.addWidget(versionLabel, 0, 0, 1, 1)
        updateWidgetLayout.addWidget(updateText, 1, 0, 1, 3)
        updateWidgetLayout.addWidget(ok, 2, 2, 1, 1)
        updateWidgetLayout.addWidget(cancel, 2, 1, 1, 1)
        updateWidget.setLayout(updateWidgetLayout)
        UpdateWindow.update.setCentralWidget(updateWidget)
        UpdateWindow.update.setWindowTitle("检查 UEngine 运行器更新")
        UpdateWindow.update.setWindowIcon(QtGui.QIcon(iconPath))
        UpdateWindow.update.resize(int(updateWidget.frameGeometry().width()), int(updateWidget.frameGeometry().height() * 1.5))
        UpdateWindow.update.show()

    def Update():
        if os.path.exists("/tmp/uengine-runner/update"):
            shutil.rmtree("/tmp/uengine-runner/update")
        os.makedirs("/tmp/uengine-runner/update")
        try:            
            print(UpdateWindow.data["Url"])
            write_txt("/tmp/uengine-runner/update.sh", f"""#!/bin/bash
echo 删除多余的安装包
rm -rfv /tmp/uengine-runner/update/*
echo 关闭“UEngine 运行器”
python3 "{programPath}/updatekiller.py"
echo 下载安装包
wget -P /tmp/uengine-runner/update {UpdateWindow.data["Url"][0]}
echo 安装安装包
dpkg -i /tmp/uengine-runner/update/*
echo 修复依赖关系
apt install -f -y
notify-send -i "{iconPath}" "更新完毕！"
zenity --info --text=\"更新完毕！\" --ellipsize
""")
        except:
            traceback.print_exc()
            QtWidgets.QMessageBox.critical(widget, "错误，无法继续更新", traceback.format_exc())
        OpenTerminal(f"pkexec bash /tmp/uengine-runner/update.sh")
        
image = None
class ApkInformation():
    message = None
    def ShowWindows():
        global fullInformation
        global path
        global tab1
        path = ComboInstallPath.currentText()
        package = GetApkPackageName(path)
        if package == None or package == "":
            QtWidgets.QMessageBox.critical(widget, "错误", langFile[lang]["Main"]["MainWindow"]["Error"]["ApkFileError"])
            return
        ApkInformation.message = QtWidgets.QMainWindow()
        messageWidget = QtWidgets.QWidget()
        messageLayout = QtWidgets.QVBoxLayout()
        ApkInformation.message.setWindowTitle("“{}“的Apk信息".format(GetApkChineseLabel(path)))
        tab = QtWidgets.QTabWidget()

        tab1 = QtWidgets.QWidget()
        tab2 = QtWidgets.QWidget()

        tab.addTab(tab1, "简化版")
        tab1Layout = QtWidgets.QGridLayout()
        SaveApkIcon(path, "/tmp/uengine-runner-android-app-icon.png")
        simpleInformation = QtWidgets.QLabel(f"""
<p align='center'><img width='256' src='/tmp/uengine-runner-android-app-icon.png'></p>
<p>包名：{GetApkPackageName(path)}</p>
<p>中文名：{GetApkChineseLabel(path)}</p>
<p>Activity：{GetApkActivityName(path)}</p>
<p>版本：{GetApkVersion(path)}</p>""")

        seeFen = QtWidgets.QPushButton("查看程序评分情况")
        updFen = QtWidgets.QPushButton("上传程序评分情况")
        seeFen.setEnabled(map)
        seeFen.clicked.connect(ApkInformation.ShowMap)
        updFen.clicked.connect(ApkInformation.UpdateMark)
        tab1Layout.addWidget(simpleInformation, 0, 0, 1, 3)
        tab1Layout.addWidget(seeFen, 1, 1, 1, 1)
        tab1Layout.addWidget(updFen, 2, 1, 1, 1)
        tab1.setLayout(tab1Layout)

        tab.addTab(tab2, "完整版")
        tab2Layout = QtWidgets.QVBoxLayout()
        fullInformation = QtWidgets.QTextBrowser()
        fullInformation.setText(GetApkInformation(path))
        tab2Layout.addWidget(fullInformation)
        tab2.setLayout(tab2Layout)

        messageLayout.addWidget(tab)
        messageWidget.setLayout(messageLayout)
        ApkInformation.message.setCentralWidget(messageWidget)
        ApkInformation.message.setWindowIcon(QtGui.QIcon(iconPath))
        ApkInformation.message.setWindowTitle("APK 信息")
        ApkInformation.message.show()
        return

    def UpdateMark():
        chooseWindow = QtWidgets.QMessageBox()
        chooseWindow.setWindowTitle("选择评分")
        chooseWindow.setText(f"""选择应用“{GetApkChineseLabel(path)}”的使用评分。建议参考如下规范进行评分：
含有不良信息（-1分）：含有违法违规信息（如果有就不要选择其它选项了）
0星：完全无法使用，连安装都有问题
1星：完全无法使用，但是能正常安装
2星：可以打开，但只能使用一点点功能
3星：勉强能使用，运行也不大流畅
4星：大部分功能正常，运行流畅（可能会有点小卡）
5星：完全正常且非常流畅，没有任何功能和性能问题，就和直接在手机上用一样
""")
        choices=["含有不良信息", "0分", "1分", "2分", "3分", "4分", "5分", "取消"]
        button0 = chooseWindow.addButton(choices[0], QtWidgets.QMessageBox.ActionRole)
        button1 = chooseWindow.addButton(choices[1], QtWidgets.QMessageBox.ActionRole)
        button2 = chooseWindow.addButton(choices[2], QtWidgets.QMessageBox.ActionRole)
        button3 = chooseWindow.addButton(choices[3], QtWidgets.QMessageBox.ActionRole)
        button4 = chooseWindow.addButton(choices[4], QtWidgets.QMessageBox.ActionRole)
        button5 = chooseWindow.addButton(choices[5], QtWidgets.QMessageBox.ActionRole)
        button6 = chooseWindow.addButton(choices[6], QtWidgets.QMessageBox.ActionRole)
        button7 = chooseWindow.addButton(choices[7], QtWidgets.QMessageBox.ActionRole)
        button0.clicked.connect(lambda: ApkInformation.UpdateMarkInternet(int(0)))
        button1.clicked.connect(lambda: ApkInformation.UpdateMarkInternet(int(1)))
        button2.clicked.connect(lambda: ApkInformation.UpdateMarkInternet(int(2)))
        button3.clicked.connect(lambda: ApkInformation.UpdateMarkInternet(int(3)))
        button4.clicked.connect(lambda: ApkInformation.UpdateMarkInternet(int(4)))
        button5.clicked.connect(lambda: ApkInformation.UpdateMarkInternet(int(5)))
        button6.clicked.connect(lambda: ApkInformation.UpdateMarkInternet(int(6)))
        button7.clicked.connect(lambda: ApkInformation.UpdateMarkInternet(int(7)))
        chooseWindow.exec_()
        return
    
    def UpdateMarkInternet(choose):
        print(choose)
        if choose == None or choose == 7:
            return
        try:
            QtWidgets.QMessageBox.information(widget, "提示", requests.post("http://120.25.153.144/uengine-runner/app/check/add.php", {"Package": GetApkPackageName(path), "Type": choose}).text)
        except:
            traceback.print_exc()
            QtWidgets.QMessageBox.critical(widget, "错误", langFile[lang]["Main"]["MainWindow"]["Error"]["ConnectServerStarError"])


    def ShowMap():
        package = GetApkPackageName(path)
        if package == None or package == "":
            QtWidgets.QMessageBox.critical(widget, "错误", langFile[lang]["Main"]["MainWindow"]["Error"]["ApkFileError"])
            return
        try:
            data = json.loads(requests.get("http://data.download.gfdgdxi.top/uengineapp/" + package +"/data.json").text)
            print(data)
        except:
            QtWidgets.QMessageBox.information(widget, "提示", "此程序暂时没有评分，欢迎您贡献第一个评分！")
            return
        index = numpy.arange(len(data))
        print(index)
        chinese = GetApkChineseLabel(path)
        fig = matplotlib.pylab.figure()
        fig.canvas.set_window_title("“" + chinese + "”的用户评分（数据只供参考）")
        fonts = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')  # 用于支持中文显示，需要依赖fonts-noto-cjk
        matplotlib.pylab.barh(index, data)
        matplotlib.pylab.yticks(index, ["不良信息", "0分", "1分", "2分", "3分", "4分", "5分"], fontproperties=fonts)
        matplotlib.pylab.xlabel("用户评分数", fontproperties=fonts)
        matplotlib.pylab.ylabel("等级", fontproperties=fonts)
        matplotlib.pylab.title("“" + chinese + "”的用户评分（数据只供参考）", fontproperties=fonts)
        matplotlib.pylab.show(block=True)

class AdbChangeUengineDisplaySize():
    messageWindow = None
    def ShowWindows():
        global displayX
        global displayY
        global displaySize
        AdbChangeUengineDisplaySize.messageWindow = QtWidgets.QMainWindow()
        message = QtWidgets.QWidget()
        messageLayout = QtWidgets.QGridLayout()

        displaySize = QtWidgets.QLabel("当前 UEngine 屏幕分辨率：\n" + subprocess.getoutput("adb -s '192.168.250.2:5555' shell wm size"))
        displayX = QtWidgets.QLineEdit()
        displayY = QtWidgets.QLineEdit()
        setButton = QtWidgets.QPushButton("设置分辨率")
        setButton.setSizePolicy(size)
        setButton.clicked.connect(AdbChangeUengineDisplaySize.SettingDisplaySize)
        messageLayout.addWidget(displaySize, 0, 0, 1, 3)
        messageLayout.addWidget(displayX, 1, 0, 1, 1)
        messageLayout.addWidget(QtWidgets.QLabel("×"))
        messageLayout.addWidget(displayY, 1, 2, 1, 1)
        messageLayout.addWidget(setButton, 2, 0, 1, 3, QtCore.Qt.AlignCenter)


        message.setLayout(messageLayout)
        AdbChangeUengineDisplaySize.messageWindow.setCentralWidget(message)
        AdbChangeUengineDisplaySize.messageWindow.setWindowTitle("修改 UEngine 分辨率")
        AdbChangeUengineDisplaySize.messageWindow.setWindowIcon(QtGui.QIcon(iconPath))
        AdbChangeUengineDisplaySize.messageWindow.show()
        return

    def GetUengineDisplaySize():
        global displaySize
        displaySize.setText("当前 UEngine 屏幕分辨率：\n" + subprocess.getoutput("adb -s '192.168.250.2:5555' shell wm size"))

    def SettingDisplaySize():
        global displayX
        global displayY
        try:
            int(displayX.text())
            int(displayY.text())
        except:
            QtWidgets.QMessageBox.critical(widget, "错误", langFile[lang]["Main"]["MainWindow"]["Error"]["InputDataError"])
            return
        os.system("adb -s '192.168.250.2:5555' shell wm size {}x{}".format(displayX.text(), displayY.text()))
        AdbChangeUengineDisplaySize.GetUengineDisplaySize()
        QtWidgets.QMessageBox.information(widget, "提示", "执行完毕！")

class ShowTextTipsWindow():
    messageWindow = None
    def ShowWindow(things):
        ShowTextTipsWindow.messageWindow = QtWidgets.QMainWindow()
        message = QtWidgets.QWidget()
        messageLayout = QtWidgets.QVBoxLayout()

        text = QtWidgets.QTextBrowser()
        text.setText(things)
        ok = QtWidgets.QPushButton("确定")
        ok.clicked.connect(ShowTextTipsWindow.messageWindow.close)
        #ok.setSizePolicy(size)

        messageLayout.addWidget(text)
        messageLayout.addWidget(ok)

        message.setLayout(messageLayout)
        ShowTextTipsWindow.messageWindow.setCentralWidget(message)
        ShowTextTipsWindow.messageWindow.setWindowTitle("提示")
        ShowTextTipsWindow.messageWindow.setWindowIcon(QtGui.QIcon(iconPath))
        ShowTextTipsWindow.messageWindow.show()
        ShowTextTipsWindow.messageWindow.resize(int(ShowTextTipsWindow.messageWindow.frameSize().width() * 2), int(ShowTextTipsWindow.messageWindow.frameSize().height() * 1.5))
        return

# 添加/删除 uengine 应用快捷方式
class AddNewUengineDesktopLink():
    addTips = '''可以输入app的包名和Activity或通过浏览apk文件来获取包名和Activity
注意：如果是要删除只要输入包名即可'''
    messageWindow = None
    def ShowWindow():
        global activityName
        global packageName
        AddNewUengineDesktopLink.messageWindow = QtWidgets.QMainWindow()
        message = QtWidgets.QWidget()
        messageLayout = QtWidgets.QGridLayout()

        activityName = QtWidgets.QLineEdit()
        packageName = QtWidgets.QLineEdit()
        browser = QtWidgets.QPushButton("浏览……")
        controlFrame = QtWidgets.QHBoxLayout()
        open = QtWidgets.QPushButton("打开")
        save = QtWidgets.QPushButton("保存")
        delete = QtWidgets.QPushButton("删除")

        packageName.setPlaceholderText("APK 包名")
        activityName.setPlaceholderText("APK 的 Activity")
        
        browser.clicked.connect(AddNewUengineDesktopLink.FindApk)
        open.clicked.connect(AddNewUengineDesktopLink.TestOpen)
        save.clicked.connect(AddNewUengineDesktopLink.SaveDesktopLink)
        delete.clicked.connect(AddNewUengineDesktopLink.DelDesktopLink)

        messageLayout.addWidget(QtWidgets.QLabel(AddNewUengineDesktopLink.addTips), 0, 0, 1, 3)
        messageLayout.addWidget(packageName, 1, 0, 1, 1)
        messageLayout.addWidget(activityName, 1, 1, 1, 1)
        messageLayout.addWidget(browser, 1, 2, 1, 1)
        messageLayout.addLayout(controlFrame, 2, 0, 1, 3)
        controlFrame.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        controlFrame.addWidget(open)
        controlFrame.addWidget(save)
        controlFrame.addWidget(delete)
        controlFrame.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        message.setLayout(messageLayout)
        AddNewUengineDesktopLink.messageWindow.setCentralWidget(message)
        AddNewUengineDesktopLink.messageWindow.setWindowTitle("添加/删除 UEngine 图标")
        AddNewUengineDesktopLink.messageWindow.setWindowIcon(QtGui.QIcon(iconPath))
        AddNewUengineDesktopLink.messageWindow.show()
        return

    # 添加快捷方式
    def SaveDesktopLink():
        try:
            if os.path.exists("{}/{}.desktop".format(desktopFilePath, packageName.text())):
                if QtWidgets.QMessageBox.question(widget, "提示", "文件已存在，是否要覆盖？") == QtWidgets.QMessageBox.No:
                    return
            if not os.path.exists("{}/.local/share/icons/hicolor/256x256/apps/".format(get_home())):
                os.makedirs("{}/.local/share/icons/hicolor/256x256/apps/".format(get_home()))
            global activityName
            iconSavePath = "{}/.local/share/icons/hicolor/256x256/apps/{}.png".format(get_home(), packageName.text())
            shutil.copy(programPath + "/defult.png", iconSavePath)
            BuildUengineDesktop(packageName.text(), activityName.text(), packageName.text(), iconSavePath,
                "{}/{}.desktop".format(desktopFilePath, packageName.text()))
            BuildUengineDesktop(packageName.text(), activityName.text(), packageName.text(), iconSavePath,
                "{}/{}.desktop".format(get_desktop_path(), packageName.text()))
            AddNewUengineDesktopLink.SaveHistory()
            QtWidgets.QMessageBox.information(widget, "提示", "创建完毕！")
        except:
            traceback.print_exc()
            QtWidgets.QMessageBox.information(widget, "错误", traceback.format_exc())


    # 删除快捷方式
    def DelDesktopLink():
        try:
            global packageName
            if not os.path.exists("{}/{}.desktop".format(desktopFilePath, packageName.text())):
                QtWidgets.QMessageBox.critical(widget, "错误", "此包名对应的 UEngine 快捷方式不存在！")
                return
            if QtWidgets.QMessageBox.warning(widget, "警告", "你确定要删除吗？删除后将无法恢复！", QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel) == QtWidgets.QMessageBox.Cancel:
                return
            try:
                os.remove("{}/{}.desktop".format(desktopFilePath, packageName.text()))
                AddNewUengineDesktopLink.SaveHistory()
                QtWidgets.QMessageBox.information(widget, "提示", "已删除")
            except:
                traceback.print_exc()
                QtWidgets.QMessageBox.critical(widget, "错误", traceback.format_exc())
        except:
            traceback.print_exc()
            QtWidgets.QMessageBox.critical(widget, "错误", traceback.format_exc())

    # 保存历史记录
    def SaveHistory():
        findApkNameHistory.append(packageName.text())
        findApkActivityHistory.append(activityName.text())
        write_txt(get_home() + "/.config/uengine-runner/FindApkNameHistory.json", str(json.dumps(ListToDictionary(findApkNameHistory))))  # 将历史记录的数组转换为字典并写入 
        write_txt(get_home() + "/.config/uengine-runner/FindApkActivityHistory.json", str(json.dumps(ListToDictionary(findApkActivityHistory))))  # 将历史记录的数组转换为字典并写入

    # 打开测试
    def TestOpen():
        threading.Thread(target=os.system, args=["/usr/bin/uengine launch --package={} --component={}".format(packageName.text(), activityName.text())]).start()
        AddNewUengineDesktopLink.SaveHistory()

    # 浏览文件
    def FindApk():
        path = QtWidgets.QFileDialog.getOpenFileName(widget, "选择apk", "~", "APK 文件(*.apk);;所有文件(*.*)", json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApkName.json"))["path"])[0]
        if path == "" or path == () or path == None:
            return
        packageName.setText(GetApkPackageName(path))
        activityName.setText(str(GetApkActivityName(path)))
        write_txt(get_home() + "/.config/uengine-runner/FindApkName.json", json.dumps({"path": os.path.dirname(path)}))  # 写入配置文件

def GetNewInformation():
    try:
        text = requests.get("http://www.gfdgdxi.top/uengine-runner/Help/information/index.html").text
        print(text)
    except:
        traceback.print_exc()
        text = """<p>无法连接到服务器</p>
            <hr/>
            <p>你可以尝试：</p>
            <p>1. 判断是否能正常连接网络</p>
            <p>2. 网络配置是否有误</p>"""
    global webInformation
    if bad:
        webInformation = QtWidgets.QTextBrowser()
    else:
        webInformation = QtWebEngineWidgets.QWebEngineView()
    webInformation.setHtml(text)
    webInformation.setWindowTitle("获取程序公告")
    webInformation.setWindowIcon(QtGui.QIcon(iconPath))
    webInformation.resize(int(webInformation.frameGeometry().width() * 1.3), int(webInformation.frameGeometry().height() * 1.1))
    webInformation.show()


def UseProgram():
    global useProgram
    useProgram = '''<p>1、UEngine：{}</p>
<p>2、python3：{}</p>
<p>3、PyQt：{}</p>
<p>4、aapt：{}</p>
<p>5、dpkg：{}</p>
<p>6、mkdir：{}</p>
<p>7、echo</p>
<p>8、chmod：{}</p>
<p>9、adb：{}</p>
<p>10、deepin 终端：{}</p>'''.format(subprocess.getoutput("uengine version"),
    subprocess.getoutput("python3 --version"),
    QtCore.qVersion,
    subprocess.getoutput(f"'{programPath}/aapt/run-aapt.sh' version"),
    subprocess.getoutput("dpkg --version"),
    subprocess.getoutput("mkdir --version"),
    subprocess.getoutput("chmod --version"),
    subprocess.getoutput("adb version"),
    subprocess.getoutput("deepin-terminal -v"))

def BackAPK(choice):
    global choose
    choose = choice

def InstallUEnginePatchForWayland():
    if os.system("which uengine"):
        QtWidgets.QMessageBox.critical(window, "错误", "未安装UEngine，请先安装UEngine")
        return
    if os.path.exists("/usr/bin/uengine-session"):
        QtWidgets.QMessageBox.critical(window, "提示", "已安装该补丁，请勿重复安装")
        return
    os.system(f"pkexec bash '{programPath}/LoadingBinder/uengine-wayland-install.sh'")
    QtWidgets.QMessageBox.information(window, "提示", "安装成功！重启电脑后生效")

def RemoveUEnginePatchForWayland():
    if os.system("which uengine"):
        QtWidgets.QMessageBox.critical(window, "错误", "未安装UEngine，请先安装UEngine")
        return
    if not os.path.exists("/usr/bin/uengine-session"):
        QtWidgets.QMessageBox.critical(window, "提示", "已卸载该补丁，无需卸载")
        return
    os.system(f"pkexec bash '{programPath}/LoadingBinder/uengine-wayland-uninstall.sh'")
    QtWidgets.QMessageBox.information(window, "提示", "卸载成功！重启电脑后生效")

###########################
# 程序信息
###########################
lang = get_now_lang()
programPath = os.path.split(os.path.realpath(__file__))[0]  # 返回 string
information = json.loads(readtxt(programPath + "/information.json"))
langFile = json.loads(readtxt(programPath + "/Language.json"))
if not lang in langFile.keys():
    lang = "en_US.UTF-8"
programUrl = information["Url"][0]
version = information["Version"]
goodRunSystem = information["System"]
aaptVersion = GetCommandReturn(f"'{programPath}/aapt/run-aapt.sh' version")
SystemVersion = GetSystemVersion()
iconPath = "{}/runner.svg".format(os.path.split(os.path.realpath(__file__))[0])
about = f'''<p>介绍：虽然通过Deepin/UOS应用商店已经能够安装部分安卓应用，但对于安卓应用爱好者来说，不能自由地安装任意APK软件包实在是不尽如人意。本软件可以实现在Deepin/UOS上安装任意APK软件包，并能将其启动图标发送到系统桌面或启动器中，方便用户快速启动它。  </p>
<p>程序开源许可证：GPLV3</p>
<p>版本：{version}</p>
<p>适用平台：{goodRunSystem}</p>
<p>Qt 版本：{QtCore.qVersion()}</p>
<p>程序官网：{programUrl}</p>
<p>系统版本：{SystemVersion}</p>
<p>安装包构建时间：{information['Time']}</p>
<p>QQ 交流群：872491938</p>
<h1>©2021-{time.strftime("%Y")} gfdgd xi</h1>'''
updateThingsString = ""
tips = ""
contribute = ""
appreciate = f"""<h3>请作者喝杯茶</h3>
<p>如果您觉得 UEngine 运行器对你有帮助，可以请作者喝杯茶 </p>
<p>
    <img src="{programPath}/Icon/QR/Wechat.png" width="250"  /> 
    <img src="{programPath}/Icon/QR/Alipay.jpg" width="250"  />
    <img src="{programPath}/Icon/QR/QQ.png" width="250" >
</p>
<hr/>
<h3>广告</h3>
<p>支付宝官方活动，扫描获得支付红包！</p>
<p><img src="{programPath}/Icon/QR/advertisement0.jpg" width="250" ></p>"""
for i in information["Tips"]:
    tips += f"<p>{i}</p>"
for i in information["Update"]:
    updateThingsString += f"<p>{i}</p>"
for i in information["Contribute"]:
    contribute += f"<p>{i}</p>"
title = "{} {}".format(langFile[lang]["Main"]["MainWindow"]["Title"], version)
updateTime = information["Time"]
updateThings = "{} 更新内容：\n{}\n更新时间：{}".format(version, updateThingsString, updateTime, time.strftime("%Y"))
desktop = programPath + "/UengineAndroidProgramList.desktop"
desktopName = "UengineAndroidProgramList.desktop"
useProgram = ""
threading.Thread(target=UseProgram).start()
isDeepin23=False
# 判断是不是 Deepin23
if os.path.exists("/etc/deepin_version"):
    try:
        with open(f"/etc/deepin_version") as file:
            isDeepin23 = "23" in file.read()
    except:
        traceback.print_exc()
desktopFilePath = f"{get_home()}/.local/share/applications/uengine/"
if isDeepin23:
    desktopFilePath = f"{get_home()}/.local/share/applications/"


###########################
# 加载配置
###########################
app = QtWidgets.QApplication(sys.argv)
if not os.path.exists(desktopFilePath):
    os.makedirs(desktopFilePath)
if not os.path.exists(get_home() + "/.config/uengine-runner"):  # 如果没有配置文件夹
    os.makedirs(get_home() + "/.config/uengine-runner")  # 创建配置文件夹
if not os.path.exists(get_home() + "/.config/uengine-runner/FindApkHistory.json"):  # 如果没有配置文件
    write_txt(get_home() + "/.config/uengine-runner/FindApkHistory.json", json.dumps({}))  # 创建配置文件
if not os.path.exists(get_home() + "/.config/uengine-runner/FindApkNameHistory.json"):  # 如果没有配置文件
    write_txt(get_home() + "/.config/uengine-runner/FindApkNameHistory.json", json.dumps({}))  # 创建配置文件
if not os.path.exists(get_home() + "/.config/uengine-runner/FindApkActivityHistory.json"):  # 如果没有配置文件
    write_txt(get_home() + "/.config/uengine-runner/FindApkActivityHistory.json", json.dumps({}))  # 创建配置文件
if not os.path.exists(get_home() + "/.config/uengine-runner/FindUninstallApkHistory.json"):  # 如果没有配置文件
    write_txt(get_home() + "/.config/uengine-runner/FindUninstallApkHistory.json", json.dumps({}))  # 创建配置文件
if not os.path.exists(get_home() + "/.config/uengine-runner/FindApkName.json"):  # 如果没有配置文件
    write_txt(get_home() + "/.config/uengine-runner/FindApkName.json", json.dumps({"path": "~"}))  # 写入（创建）一个配置文件
if not os.path.exists(get_home() + "/.config/uengine-runner/FindApk.json"):  # 如果没有配置文件
    write_txt(get_home() + "/.config/uengine-runner/FindApk.json", json.dumps({"path": "~"}))  # 写入（创建）一个配置文件
if not os.path.exists(get_home() + "/.config/uengine-runner/FindUninstallApk.json"):  # 如果没有配置文件
    write_txt(get_home() + "/.config/uengine-runner/FindUninstallApk.json", json.dumps({"path": "~"}))  # 写入（创建）一个配置文件
if not os.path.exists(get_home() + "/.config/uengine-runner/SaveApkIcon.json"):  # 如果没有配置文件
    write_txt(get_home() + "/.config/uengine-runner/SaveApkIcon.json", json.dumps({"path": "~"}))  # 写入（创建）一个配置文件
if not os.path.exists(get_home() + "/.config/uengine-runner/SaveApk.json"):  # 如果没有配置文件
    write_txt(get_home() + "/.config/uengine-runner/SaveApk.json", json.dumps({"path": "~"}))  # 写入（创建）一个配置文件
if not os.path.exists(get_home() + "/.config/uengine-runner/setting.json"):
    write_txt(get_home() + "/.config/uengine-runner/setting.json", json.dumps({"SaveApk": int(1)}))
#    choosemsg = QtWidgets.QMessageBox()
#    choosemsg.setText("""在使用本程序前，请选择安装Apk包的设置以便更好的运行，下列选项的详细介绍：
#
#不备份Apk包直接安装：适用于Deepin（旧版UEngine），安装较快，不受/tmp大小所限，但Deepin23和UOS（新版UEngine）不推荐此选项，因为安装后会自动删除Apk安装包；
#备份Apk包然后在安装后自动拷贝原先目录：适用于Deepin23和UOS（新版UEngine），安装较慢，受/tmp大小所限，安装后不会丢失Apk，Deepin（旧版UEngine）不推荐使用该选项；
#
#
#后期可以在程序主界面的菜单栏的“程序”=>“设置”里进行修改，
#如果不知道正在使用的系统是什么版本可以打开系统设置查看。
#""")
#    choosemsg.setWindowTitle("设置")
#    choose = None
#    choosemsg.addButton("不备份Apk包直接安装", QtWidgets.QMessageBox.ActionRole).clicked.connect(lambda: BackAPK(0))
#    choosemsg.addButton("备份Apk包然后在安装后自动拷贝原先目录", QtWidgets.QMessageBox.ActionRole).clicked.connect(lambda: BackAPK(1))
#    choosemsg.exec_()
#    if choose == None:
#        QtWidgets.QMessageBox.information(None, "提示", "必须选择一个选项！否则无法进入程序！")
#        sys.exit()            
#    write_txt(get_home() + "/.config/uengine-runner/setting.json", json.dumps({"SaveApk": int(choose)}))
defultProgramList = {
    "SaveApk": 1,
    "AutoScreenConfig": False,
    "ChooseProgramType": False,
    "Theme": ""
}
try:
    settingConf = json.loads(readtxt(get_home() + "/.config/uengine-runner/setting.json"))
    change = False
    for i in defultProgramList.keys():
        if not i in settingConf:
            change = True
            settingConf[i] = defultProgramList[i]
    if change:
        write_txt(get_home() + "/.config/uengine-setting.json", json.dumps(settingConf))
except:
    traceback.print_exc()
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QMessageBox.critical(None, "错误", f"无法读取配置，无法继续\n{traceback.format_exc()}")
    sys.exit(1)

###########################
# 设置变量
###########################
findApkHistory = list(json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApkHistory.json")).values())
fineUninstallApkHistory = list(json.loads(readtxt(get_home() + "/.config/uengine-runner/FindUninstallApkHistory.json")).values())
findApkNameHistory = list(json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApkNameHistory.json")).values())
findApkActivityHistory = list(json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApkActivityHistory.json")).values())

try:
    threading.Thread(target=requests.get, args=[parse.unquote(base64.b64decode("aHR0cHM6Ly8zMDQ2MjZwOTI3LmdvaG8uY28vdWVuZ2luZS1ydW5uZXIvb3Blbi9JbnN0YWxsLnBocA==").decode("utf-8")) + "?Version=" + version]).start()
except:
    pass
# add sub window
#添加窗口开启关闭开关，防止重复开启
windowflag = "close"
def Open():
    try:
        lists = json.loads(requests.get("https://data.download.gfdgdxi.top/Open-UEngine/lists.json").text)
        data = []
        for i in lists:
            data.append(int(requests.get("https://data.download.gfdgdxi.top/Open-UEngine/{}.txt".format(i)).text))
    except:
        QtWidgets.QMessageBox.critical(widget, "错误", "服务器出错！数据获取失败！")
        return
    fig = matplotlib.pylab.figure()
    fig.canvas.set_window_title("“UEngine 运行器”打开数（数据只供参考）")
    matplotlib.pylab.plot(lists, data)
    index = numpy.arange(len(lists))
    fonts = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')  # 用于支持中文显示，需要依赖fonts-noto-cjk
    matplotlib.pylab.xlabel("版本号", fontproperties=fonts)
    matplotlib.pylab.ylabel("打开数", fontproperties=fonts)
            
    matplotlib.pylab.title("“UEngine 运行器”打开数（数据只供参考）", fontproperties=fonts)
    matplotlib.pylab.show()

def Download():
    try:
        lists = json.loads(requests.get("https://data.download.gfdgdxi.top/Install-UEngine/lists.json").text)
        data = []
        for i in lists:
            data.append(int(requests.get("https://data.download.gfdgdxi.top/Install-UEngine/{}.txt".format(i)).text))
    except:
        traceback.print_exc()
        QtWidgets.QMessageBox.critical(widget, "错误", "服务器出错！数据获取失败！")
        return
    fig = matplotlib.pylab.figure()
    fig.canvas.set_window_title("“UEngine 运行器”安装数（数据只供参考）")
    matplotlib.pylab.plot(lists, data)
    index = numpy.arange(len(lists))
    fonts = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')  # 用于支持中文显示，需要依赖fonts-noto-cjk
    matplotlib.pylab.xlabel("版本号", fontproperties=fonts)
    matplotlib.pylab.ylabel("安装数", fontproperties=fonts)
            
    matplotlib.pylab.title("“UEngine 运行器”安装数（数据只供参考）", fontproperties=fonts)
    matplotlib.pylab.show()
helpWindow = None
def showhelp():
    global helpWindow
    helpWindow = QtWidgets.QMainWindow()
    helpWidget = QtWidgets.QWidget()
    helpLayout = QtWidgets.QGridLayout()

    def ChgLog():
        HelpStr.setHtml(updateThingsString)
    def ChgAbout(event):
        HelpStr.setHtml(f"<p align='center'><a href='https://www.gfdgdxi.top/ChangeIcon'><img width=256 src='{iconPath}'/></a></p>\n" + about)
    def OpenUrl(url):
        print(url.url())
        if url.url() == "https://www.gfdgdxi.top/ChangeIcon":
            ChgAboutChangeIcon()
            return
        webbrowser.open_new_tab(url.url())

    def ChgAboutChangeIcon():
        HelpStr.setHtml(f"<p align='center'><img width=256 src='{programPath}/Icon/Program/about-icon.png'/></p>\n" + about)
    def ChgDep():
        if useProgram == "":
            BtnZujian.setDisabled(True)
            return
        HelpStr.setHtml(useProgram)
    def ChgCon():
        HelpStr.setHtml(contribute)
    def ChgTips():
        HelpStr.setHtml(tips)
    def ChgAppreciate():
        HelpStr.setHtml(appreciate)
    def ChgGPLV3():
        try:
            with open(f"{programPath}/LICENSE", "r") as file:
                things = file.read()
                try:
                    HelpStr.setMarkdown(things)
                except:
                    # 旧版 QT 不支持 Markdown
                    traceback.print_exc()
                    HelpStr.setText(things)
        except:
            traceback.print_exc()
            HelpStr.setText(traceback.print_exc())
    
    BtnReadme = QtWidgets.QPushButton("使用说明")
    BtnLog = QtWidgets.QPushButton("更新内容")
    BtnZujian = QtWidgets.QPushButton("程序依赖的组件")
    BtnGongxian = QtWidgets.QPushButton("谢明列表")
    BtnAbout = QtWidgets.QPushButton("关于")
    BtnDownN = QtWidgets.QPushButton("程序下载量")
    BtnOpenN = QtWidgets.QPushButton("程序打开量")
    BtnGPLV3 = QtWidgets.QPushButton("程序开源许可证")
    appreciateButton = QtWidgets.QPushButton("赞赏作者")
    HelpStr = QtWidgets.QTextBrowser()
    HelpStr.setOpenLinks(False)
    HelpStr.setHtml(about)
    HelpStr.setOpenExternalLinks(False)
    HelpStr.anchorClicked.connect(OpenUrl)
    # 此功能从 2.0.0 后不再隐藏
    #BtnDownN.setEnabled("--彩蛋" in sys.argv)
    BtnReadme.clicked.connect(ChgTips)
    BtnLog.clicked.connect(ChgLog)
    BtnZujian.clicked.connect(ChgDep)
    BtnGongxian.clicked.connect(ChgCon)
    BtnAbout.clicked.connect(ChgAbout)
    BtnDownN.clicked.connect(Download)
    BtnGPLV3.clicked.connect(ChgGPLV3)
    BtnOpenN.clicked.connect(Open)
    appreciateButton.clicked.connect(ChgAppreciate)

    ChgTips()

    helpLayout.addWidget(BtnReadme, 0, 0, 1, 1)
    helpLayout.addWidget(BtnLog, 1, 0, 1, 1)
    helpLayout.addWidget(BtnZujian, 2, 0, 1, 1)
    helpLayout.addWidget(BtnGongxian, 3, 0, 1, 1)
    helpLayout.addWidget(BtnDownN, 4, 0, 1, 1)
    helpLayout.addWidget(BtnOpenN, 5, 0, 1, 1)
    helpLayout.addWidget(BtnGPLV3, 6, 0, 1, 1)
    helpLayout.addWidget(appreciateButton, 7, 0, 1, 1)
    helpLayout.addWidget(BtnAbout, 8, 0, 1, 1)
    helpLayout.addWidget(HelpStr, 0, 1, 11, 1)

    helpWidget.setLayout(helpLayout)
    helpWindow.setCentralWidget(helpWidget)
    helpWindow.setFixedSize(int(helpWindow.frameSize().width() * 0.9), int(helpWindow.frameSize().height() * 1.5))
    helpWindow.setWindowTitle("帮助")
    helpWindow.setWindowIcon(QtGui.QIcon(iconPath))
    # 设置背景
    helpWindow.setObjectName("helpWindow")
    helpWindow.setStyleSheet(f"QWidget#helpWindow {{background: url({programPath}/Icon/Program/about-background.png) no-repeat;background-position: left bottom;}}")
    helpWindow.show()
    return

###########################
# 检查 UEngine 是否安装
###########################
if not os.path.exists("/usr/bin/uengine"):
    # Deepin/UOS 用户
    if "deepin" in SystemVersion.lower() or "uos" in SystemVersion.lower() or subprocess.getoutput("arch").replace("\n", "").replace(" ", "") != "x86_64":
        if not "ft-" in GetCommandReturn("lscpu").lower() and GetCommandReturn("lscpu").replace(" ", "").replace("\n", "") == "aarch64":
            QtWidgets.QMessageBox.critical(None, "错误", "UEngine 运行器不支持非飞腾 CPU")
            sys.exit(1)
        if QtWidgets.QMessageBox.question(None, "提示", "您的电脑没有安装 UEngine，是否安装 UEngine 以便更好的使用\n安装完后重新启动该程序即可") == QtWidgets.QMessageBox.Yes:
            OpenTerminal(f"pkexec apt install uengine -y")
            sys.exit(0)
    # 非 Deepin/UOS 用户
    # 因为安装器出现问题，所以废弃
    else:
        #QtWidgets.QMessageBox.critical(None, "错误", "请安装 UEngine 后继续")
        #sys.exit(0)
        #if QtWidgets.QMessageBox.question(None, "提示", "您的电脑没有安装 UEngine，是否安装 UEngine 以便更好的使用\n这里将会使用 shenmo 提供的脚本进行安装\n安装完后重新启动该程序即可\n提示：无法保证此安装脚本安装的 UEngine 可以使用") == QtWidgets.QMessageBox.Yes:
        if QtWidgets.QMessageBox.question(None, "提示", "您的电脑没有安装 UEngine，是否安装 UEngine 以便更好的使用\n这里将会安装移植版本（之前由 Shenmo 编写）\n安装完后重新启动该程序即可\n提示：需要在 Ubuntu 20.04 或 debian10 及以上版本才能正常安装\nUbuntu 20.04 和 debian10 需要手动安装 dtk（≥5.5），可以从 http://dtk.gfdgdxi.top 获取") == QtWidgets.QMessageBox.Yes:
            #os.system(f"'{programPath}/launch.sh' deepin-terminal -C \"bash '{programPath}/uengine-installer'\"")
            OpenTerminal(f"bash '{programPath}/uengine-installer'")
            sys.exit(0)





###########################
# 窗口创建
###########################
window = QtWidgets.QMainWindow()
# 判断系统是不是 Deepin 23、有没有安装 Wayland 补丁、是不是 Wayland 环境
if not os.path.exists("/usr/bin/uengine-session") and isDeepin23 and os.getenv("XDG_SESSION_TYPE") == "wayland":
    # 如果是
    if QtWidgets.QMessageBox.question(None, "提示", "检测到您使用的是 Deepin 23 + Wayland 环境，建议安装 UEngine For Wayland 补丁以便能正常使用 UEngine，是否安装？") == QtWidgets.QMessageBox.Yes:
        InstallUEnginePatchForWayland()
widget = QtWidgets.QWidget()
widgetLayout = QtWidgets.QGridLayout()
# 权重
size = QtWidgets.QSizePolicy()
size.setHorizontalPolicy(0)
widgetSize = QtWidgets.QSizePolicy()
widgetSize.setVerticalPolicy(0)
# 创建控件
LabApkPath = QtWidgets.QLabel(langFile[lang]["Main"]["MainWindow"]["LabApkPath"])
ComboInstallPath = QtWidgets.QComboBox()
FrmInstallWidget = QtWidgets.QWidget()
FrmInstall = QtWidgets.QGridLayout()
BtnFindApk = QtWidgets.QPushButton(langFile[lang]["Main"]["MainWindow"]["BtnFindApk"])
BtnInstall = QtWidgets.QPushButton(langFile[lang]["Main"]["MainWindow"]["BtnInstall"])
BtnShowUengineApp = QtWidgets.QPushButton(langFile[lang]["Main"]["MainWindow"]["BtnShowUengineApp"])
BtnAppStore = QtWidgets.QPushButton("微型应用商店")
BtnUninstall = QtWidgets.QPushButton(langFile[lang]["Main"]["MainWindow"]["BtnUninstall"])
Btngeticon = QtWidgets.QPushButton(langFile[lang]["Main"]["MainWindow"]["Btngeticon"])
BtnSaveApk = QtWidgets.QPushButton(langFile[lang]["Main"]["MainWindow"]["BtnSaveApk"])
BtnApkInformation = QtWidgets.QPushButton(langFile[lang]["Main"]["MainWindow"]["BtnApkInformation"])
# 设置控件
FrmInstallWidget.setLayout(FrmInstall)
FrmInstallWidget.setSizePolicy(size)
BtnShowUengineApp.setSizePolicy(size)
BtnAppStore.setSizePolicy(size)
ComboInstallPath.setEditable(True)
ComboInstallPath.addItems(findApkHistory)
ComboInstallPath.setEditText("")
ComboInstallPath.setFixedSize(ComboInstallPath.frameSize().width() * 5, ComboInstallPath.frameSize().height())
try:
    if sys.argv[1] == "-i":
        ComboInstallPath.setCurrentText(sys.argv[2])
        print("Install Path: " + sys.argv[2])
    elif sys.argv[1] == "-u":
        ComboInstallPath.setCurrentText(sys.argv[2])
        print("Unstall Path: " + sys.argv[2])
    else:
        print("Command Format Error")
except:
    print("Not Command Or Command Format Error")
# 绑定信号
BtnFindApk.clicked.connect(FindApk)
BtnInstall.clicked.connect(Button3Install)
BtnShowUengineApp.clicked.connect(Button5Click)
BtnUninstall.clicked.connect(ButtonClick8)
Btngeticon.clicked.connect(SaveIconToOtherPath)
BtnSaveApk.clicked.connect(SaveInstallUengineApp)
BtnApkInformation.clicked.connect(ApkInformation.ShowWindows)
BtnAppStore.clicked.connect(lambda: threading.Thread(target=os.system, args=[f"python3 '{programPath}/AutoConfig.py'"]).start())
# 布局控件
widgetLayout.addWidget(LabApkPath, 0, 0, 1, 3)
widgetLayout.addWidget(ComboInstallPath, 1, 0, 1, 3)
widgetLayout.addWidget(BtnShowUengineApp, 2, 0, 1, 1)
widgetLayout.addWidget(BtnAppStore, 2, 1, 1, 1)
widgetLayout.addWidget(FrmInstallWidget, 0, 3, 3, 1)
FrmInstall.addWidget(BtnFindApk, 0, 0, 1, 1)
FrmInstall.addWidget(BtnInstall, 0, 1, 1, 1)
FrmInstall.addWidget(BtnUninstall, 1, 0, 1, 1)
FrmInstall.addWidget(Btngeticon, 1, 1, 1, 1)
FrmInstall.addWidget(BtnSaveApk, 2, 0, 1, 1)
FrmInstall.addWidget(BtnApkInformation, 2, 1, 1, 1)
# 设置菜单栏
menu = window.menuBar()
programmenu = menu.addMenu(langFile[lang]["Main"]["MainWindow"]["Menu"][0]["Name"])
adb = menu.addMenu(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Name"])
uengine = menu.addMenu(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Name"])
help = menu.addMenu("关于")

cleanProgramHistory = QtWidgets.QAction(QtWidgets.QApplication.style().standardIcon(47), langFile[lang]["Main"]["MainWindow"]["Menu"][0]["Menu"][0])
settingWindow = QtWidgets.QAction(QtGui.QIcon.fromTheme("settings"), langFile[lang]["Main"]["MainWindow"]["Menu"][0]["Menu"][2])
exitProgram = QtWidgets.QAction(QtGui.QIcon.fromTheme("exit"), langFile[lang]["Main"]["MainWindow"]["Menu"][0]["Menu"][1])
programmenu.addAction(cleanProgramHistory)
programmenu.addAction(settingWindow)
programmenu.addSeparator()
programmenu.addAction(exitProgram)
# 绑定事件
cleanProgramHistory.triggered.connect(CleanProgramHistory)
settingWindow.triggered.connect(SettingWindow.ShowWindow)
exitProgram.triggered.connect(window.close)

adbUengineConnect = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][0])
adbConnectDevice = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][2])
adbChangeUengineDisplaySize = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][3])
adbAndroidInstallAppList = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][4])
adbTop = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][5])
adbShell = QtWidgets.QAction(QtGui.QIcon.fromTheme("terminal"), langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][6])
adbScrcpyConnectUengine = QtWidgets.QAction(QtGui.QIcon.fromTheme("guiscrcpy"), langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][7])
adb.addAction(adbUengineConnect)
adb.addSeparator()
adbServer = adb.addMenu(QtGui.QIcon.fromTheme("services"), langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][1]["Name"])
adb.addAction(adbConnectDevice)
adb.addSeparator()
adb.addAction(adbChangeUengineDisplaySize)
adb.addAction(adbAndroidInstallAppList)
adb.addAction(adbTop)
adb.addAction(adbShell)
adb.addAction(adbScrcpyConnectUengine)
adb.addSeparator()
uengineUseAdbm = adb.addMenu(QtGui.QIcon.fromTheme("services"), langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][8]["Name"])
adbStartServer = QtWidgets.QAction(QtGui.QIcon.fromTheme("services"), langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][1]["Menu"][0])
adbStopServer = QtWidgets.QAction(QtGui.QIcon.fromTheme("services"), langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][1]["Menu"][1])
adbKillAdbProgress = QtWidgets.QAction(QtGui.QIcon.fromTheme("services"), langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][1]["Menu"][2])
uengineConnectAdb = QtWidgets.QAction(QtGui.QIcon.fromTheme("services"), langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][8]["Menu"][0])
uengineUseAdb = QtWidgets.QAction(QtGui.QIcon.fromTheme("services"), langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][8]["Menu"][1])
uengineDoNotUseAdb = QtWidgets.QAction(QtGui.QIcon.fromTheme("services"), langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][8]["Menu"][2])
# 绑定信号
uengineConnectAdb.triggered.connect(UengineConnectAdb)
adbConnectDevice.triggered.connect(AdbConnectDeviceShow)
adbChangeUengineDisplaySize.triggered.connect(AdbChangeUengineDisplaySize.ShowWindows)
adbAndroidInstallAppList.triggered.connect(AdbAndroidInstallAppList)
adbTop.triggered.connect(AdbCPUAndRAWShowInTer)
adbShell.triggered.connect(AdbShellShowInTer)
adbScrcpyConnectUengine.triggered.connect(ScrcpyConnectUengine)

adbServer.addAction(adbStartServer)
adbServer.addAction(adbStopServer)
adbServer.addAction(adbKillAdbProgress)
# 绑定信号
adbStartServer.triggered.connect(AdbStartServer)
adbStopServer.triggered.connect(AdbStopServer)
adbKillAdbProgress.triggered.connect(AdbKillAdbProgress)

uengineUseAdbm.addAction(uengineConnectAdb)
uengineUseAdbm.addAction(uengineUseAdb)
uengineUseAdbm.addSeparator()
uengineUseAdbm.addAction(uengineDoNotUseAdb)
# 绑定信号
uengineConnectAdb.triggered.connect(UengineConnectAdb)
uengineUseAdb.triggered.connect(UengineUseAdb)
uengineDoNotUseAdb.triggered.connect(UengineDoNotUseAdb)

uengineAllowOrDisallowUpdateAndroidApp = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][13])
uengineSetHttpProxy = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][15])
uengineOpenDebBuilder = QtWidgets.QAction(QtGui.QIcon.fromTheme("deb"), "UEngine 应用打包器（简单版）")
uengineOpenDebBuilderMore = QtWidgets.QAction(QtGui.QIcon.fromTheme("deb"), "UEngine 应用打包器（高级版）")
uengineKeyboardToMouse = QtWidgets.QAction(QtGui.QIcon.fromTheme("keyboard"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][7])
uengineCheckCpu = QtWidgets.QAction(QtGui.QIcon.fromTheme("cpu"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][8])
#uengineUbuntuInstall = QtWidgets.QAction(QtGui.QIcon.fromTheme("ubuntu-logo-icon"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][12])
uengineDeleteUengineCheck = QtWidgets.QAction(QtWidgets.QApplication.style().standardIcon(40), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][9])
uengineReinstall = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][10])
uengineUbuntuInstall = QtWidgets.QAction(QtGui.QIcon.fromTheme("ubuntu-logo-icon"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][14])
uengineUbuntuRemove = QtWidgets.QAction(QtGui.QIcon.fromTheme("ubuntu-logo-icon"), "移除在 Ubuntu/Debian 上安装的 UEngine 及其附属脚本")
uengineUbuntuInstallRoot = QtWidgets.QAction(QtGui.QIcon.fromTheme("ubuntu-logo-icon"), "在 Ubuntu/Debian 上安装 UEngine（SuperSU 镜像）")
uengineWindowSizeSetting = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][16])
uengineInstallVia = QtWidgets.QAction("安装 Via")
installUEnginePatchForWayland = QtWidgets.QAction("安装 UEngine For Wayland 补丁")
uninstallUEnginePatchForWayland = QtWidgets.QAction("卸载 UEngine For Wayland 补丁")
uengine.addAction(uengineOpenDebBuilder)
uengine.addAction(uengineOpenDebBuilderMore)
uengine.addAction(uengineKeyboardToMouse)
uengine.addAction(uengineCheckCpu)
uengine.addSeparator()
uengine.addAction(uengineUbuntuInstall)
uengine.addAction(uengineUbuntuInstallRoot)
uengine.addAction(uengineUbuntuRemove)
uengine.addSeparator()
uengine.addAction(uengineWindowSizeSetting)
uengine.addSeparator()
uengine.addAction(uengineAllowOrDisallowUpdateAndroidApp)
uengine.addAction(uengineSetHttpProxy)
uengine.addSeparator()
uengineService = uengine.addMenu(QtGui.QIcon.fromTheme("services"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][2]["Name"])
uengineInternet = uengine.addMenu(QtGui.QIcon.fromTheme("internet"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Name"])
uengine.addSeparator()
uengineIcon = uengine.addMenu(QtGui.QIcon.fromTheme("desktop"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Name"])
uengine.addSeparator()
uengine.addMenu(uengineUseAdbm)
uengineData = uengine.addMenu(QtGui.QIcon.fromTheme("fileopen"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][6]["Name"])
uengine.addSeparator()
uengine.addAction(uengineDeleteUengineCheck)
uengine.addAction(uengineReinstall)
uengineRoot = uengine.addMenu(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][11]["Name"])
uengine.addSeparator()
uengine.addAction(uengineInstallVia)
uengine.addSeparator()
uengine.addAction(installUEnginePatchForWayland)
uengine.addAction(uninstallUEnginePatchForWayland)

#uengineUbuntuInstall.setDisabled(True)
# 绑定信号
uengineAllowOrDisallowUpdateAndroidApp.triggered.connect(AllowOrDisallowUpdateAndroidApp)
uengineSetHttpProxy.triggered.connect(SetHttpProxy)
uengineUbuntuRemove.triggered.connect(lambda: threading.Thread(target=OpenTerminal, args=[f"bash '{programPath}/uengine-remove.sh'"]).start())
uengineOpenDebBuilder.triggered.connect(OpenUengineDebBuilder)
uengineOpenDebBuilderMore.triggered.connect(lambda: threading.Thread(target=os.system, args=[f"'{programPath}/uengine-apk-builder-more'"]).start())
uengineKeyboardToMouse.triggered.connect(KeyboardToMouse)
uengineCheckCpu.triggered.connect(UengineCheckCpu)
uengineUbuntuInstall.triggered.connect(UengineUbuntuInstall)
uengineUbuntuInstallRoot.triggered.connect(UengineUbuntuInstallRoot)
uengineDeleteUengineCheck.triggered.connect(DelUengineCheck)
uengineReinstall.triggered.connect(ReinstallUengine)
uengineWindowSizeSetting.triggered.connect(UengineWindowSizeSetting.ShowWindow)
installUEnginePatchForWayland.triggered.connect(InstallUEnginePatchForWayland)
uninstallUEnginePatchForWayland.triggered.connect(RemoveUEnginePatchForWayland)

def InstallVia():
    ComboInstallPath.setCurrentText(f"{programPath}/APK/Via.apk")
    Button3Install()

uengineInstallVia.triggered.connect(InstallVia)

uengineStart = QtWidgets.QAction(QtGui.QIcon.fromTheme("services"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][2]["Menu"][0])
uengineStop = QtWidgets.QAction(QtGui.QIcon.fromTheme("services"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][2]["Menu"][1])
uengineRestart = QtWidgets.QAction(QtGui.QIcon.fromTheme("services"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][2]["Menu"][2])
uengineService.addAction(uengineStart)
uengineService.addAction(uengineStop)
uengineService.addAction(uengineRestart)
# 绑定信号
uengineStart.triggered.connect(StartUengine)
uengineStop.triggered.connect(StopUengine)
uengineRestart.triggered.connect(UengineRestart)

uengineBridgeStart = QtWidgets.QAction(QtGui.QIcon.fromTheme("internet"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][0])
uengineBridgeStop = QtWidgets.QAction(QtGui.QIcon.fromTheme("internet"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][1])
uengineBridgeRestart = QtWidgets.QAction(QtGui.QIcon.fromTheme("internet"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][2])
uengineBridgeReload = QtWidgets.QAction(QtGui.QIcon.fromTheme("internet"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][3])
uengineBridgeForceReload = QtWidgets.QAction(QtGui.QIcon.fromTheme("internet"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][4])
uengineInternet.addAction(uengineBridgeStart)
uengineInternet.addAction(uengineBridgeStop)
#uengineInternet.addAction(uengineReinstall)
uengineInternet.addAction(uengineBridgeReload)
uengineInternet.addAction(uengineBridgeForceReload)
# 绑定信号
uengineBridgeStart.triggered.connect(UengineBridgeStart)
uengineBridgeStop.triggered.connect(UengineBridgeStop)
uengineBridgeRestart.triggered.connect(UengineBridgeRestart)
uengineBridgeReload.triggered.connect(UengineBridgeReload)
uengineBridgeForceReload.triggered.connect(UengineBridgeForceReload)

uengineSendUengineAndroidListForDesktop = QtWidgets.QAction(QtGui.QIcon.fromTheme("desktop"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Menu"][0])
uengineSendUengineAndroidListForLauncher = QtWidgets.QAction(QtGui.QIcon.fromTheme("desktop"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Menu"][1])
uengineAddNewUengineDesktopLink = QtWidgets.QAction(QtGui.QIcon.fromTheme("desktop"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Menu"][2])
uengineCleanAllUengineDesktopLink = QtWidgets.QAction(QtGui.QIcon.fromTheme("desktop"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Menu"][3])
uengineIcon.addAction(uengineSendUengineAndroidListForDesktop)
uengineIcon.addAction(uengineSendUengineAndroidListForLauncher)
uengineIcon.addSeparator()
uengineIcon.addAction(uengineAddNewUengineDesktopLink)
uengineIcon.addSeparator()
uengineIcon.addAction(uengineCleanAllUengineDesktopLink)
# 绑定信号
uengineSendUengineAndroidListForDesktop.triggered.connect(SendUengineAndroidListForDesktop)
uengineSendUengineAndroidListForLauncher.triggered.connect(SendUengineAndroidListForLauncher)
uengineAddNewUengineDesktopLink.triggered.connect(AddNewUengineDesktopLink.ShowWindow)
uengineCleanAllUengineDesktopLink.triggered.connect(CleanAllUengineDesktopLink)

#uengineData
uengineOpenRootData = QtWidgets.QAction(QtGui.QIcon.fromTheme("fileopen"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][6]["Menu"][0])
uengineOpenUserData = QtWidgets.QAction(QtGui.QIcon.fromTheme("fileopen"), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][6]["Menu"][1])
uengineBackClean = QtWidgets.QAction(QtWidgets.QApplication.style().standardIcon(40), langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][6]["Menu"][2])
uengineData.addAction(uengineOpenRootData)
uengineData.addAction(uengineOpenUserData)
uengineData.addSeparator()
uengineData.addAction(uengineBackClean)
# 绑定信号
uengineOpenRootData.triggered.connect(OpenUengineRootData)
uengineOpenUserData.triggered.connect(OpenUengineUserData)
uengineBackClean.triggered.connect(BackUengineClean)

#uengineRoot
uengineInstallRootUengineImage = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][11]["Menu"][0])
uengineBuildRootUengineImage = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][11]["Menu"][1])
uengineReinstallUengineImage = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][11]["Menu"][2])
uengineRoot.addAction(uengineInstallRootUengineImage)
uengineRoot.addAction(uengineBuildRootUengineImage)
uengineRoot.addSeparator()
uengineRoot.addAction(uengineReinstallUengineImage)
# 绑定信号
uengineInstallRootUengineImage.triggered.connect(InstallRootUengineImage)
uengineBuildRootUengineImage.triggered.connect(BuildRootUengineImage)
uengineReinstallUengineImage.triggered.connect(ReinstallUengineImage)

helpOpenProgramUrl = QtWidgets.QAction(QtWidgets.QApplication.style().standardIcon(20), langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][0])
makerWebsize = QtWidgets.QAction(QtWidgets.QApplication.style().standardIcon(20), "作者个人站")
uengineRunnerSearch = QtWidgets.QAction(QtWidgets.QApplication.style().standardIcon(20), "查询指定程序在 UEngine 的运行情况")
helpUengineRunnerBugUpload = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][2])
helpShowHelp = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][4])
helpRunnerUpdate = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][3])
helpFen = QtWidgets.QAction("程序评分")
helpWebInformation = QtWidgets.QAction("程序公告")
helpAbout = QtWidgets.QAction(QtWidgets.QApplication.style().standardIcon(9), "关于")
helpAboutQt = QtWidgets.QAction(QtWidgets.QApplication.style().standardIcon(9), langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][5])
help.addAction(helpOpenProgramUrl)
help.addAction(uengineRunnerSearch)
help.addAction(makerWebsize)
help.addSeparator()
help.addAction(helpUengineRunnerBugUpload)
help.addSeparator()
help.addAction(helpShowHelp)
help.addAction(helpRunnerUpdate)
help.addAction(helpFen)
help.addAction(helpWebInformation)
help.addSeparator()
help.addAction(helpAbout)
help.addAction(helpAboutQt)
help.addSeparator()
hm1 = help.addMenu("更多生态适配应用")
hm1_1 = QtWidgets.QAction("运行 Windows 应用：Wine 运行器")
hm1.addAction(hm1_1)
hm1_1.triggered.connect(lambda: webbrowser.open_new_tab("https://gitee.com/gfdgd-xi/deep-wine-runner"))
# 绑定信号
helpOpenProgramUrl.triggered.connect(OpenProgramURL)
uengineRunnerSearch.triggered.connect(lambda: webbrowser.open_new_tab("https://gfdgd-xi.github.io/uengine-runner-info/"))
makerWebsize.triggered.connect(lambda: webbrowser.open_new_tab("https://gfdgd-xi.github.io"))
helpUengineRunnerBugUpload.triggered.connect(UengineRunnerBugUpload)
helpShowHelp.triggered.connect(ShowHelp)
helpRunnerUpdate.triggered.connect(UpdateWindow.ShowWindow)
helpFen.triggered.connect(lambda: threading.Thread(target=os.system, args=[f"'{programPath}/ProgramFen.py'"]).start())
helpWebInformation.triggered.connect(GetNewInformation)
helpAbout.triggered.connect(showhelp)
helpAboutQt.triggered.connect(lambda: QtWidgets.QMessageBox.aboutQt(widget))

# 设置窗口
app.setStyle(QtWidgets.QStyleFactory.create(settingConf["Theme"]))
widget.setLayout(widgetLayout)
window.setCentralWidget(widget)
window.setWindowTitle(title)
window.show()
window.setWindowIcon(QtGui.QIcon(iconPath))
window.setFixedSize(window.frameSize().width(), window.frameSize().height())
sys.exit(app.exec_())
