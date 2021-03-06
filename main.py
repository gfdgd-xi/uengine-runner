#!/usr/bin/env python3
# 使用系统默认的 python3 运行
###########################################################################################
# 作者：gfdgd xi<3025613752@qq.com>
# 版本：1.8.0
# 更新时间：2022年07月23日
# 感谢：anbox、deepin 和 UOS
# 基于 Python3 的 tkinter 构建
# 更新：gfdgd xi<3025613752@qq.com>、actionchen<917981399@qq.com>、为什么您不喜欢熊出没和阿布呢
###########################################################################################
#################
# 引入所需的库
#################
import os
import api
import sys
import time
import json
import shutil
import zipfile
import traceback
import threading
import easygui
import ttkthemes
import webbrowser
import subprocess
import matplotlib
import requests
import numpy
import matplotlib.figure
import matplotlib.pylab
import matplotlib.font_manager
import PIL.Image as Image
import PIL.ImageTk as ImageTk
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import tkinter.simpledialog as simpledialog
from getxmlimg import getsavexml

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
            Return = os.system("pkexec /usr/bin/uengine-session-launch-helper -- uengine uninstall --pkg='{}'".format(package))
            print(Return)
            if Return != 0:
                self.error.emit("疑似卸载失败，请检查 UEngine 是否正常安装、运行以及 APK 文件或包名是否正确、完整")
                DisabledAndEnbled(False)
                return
            if os.path.exists("{}/.local/share/applications/uengine/{}.desktop".format(get_home(), package)):
                os.remove("{}/.local/share/applications/uengine/{}.desktop".format(get_home(), package))
            if os.path.exists("{}/{}.desktop".format(get_desktop_path(), package)):
                os.remove("{}/{}.desktop".format(get_desktop_path(), package))
            findApkHistory.append(ComboInstallPath.currentText())
            self.combo.emit(0)
            write_txt(get_home() + "/.config/uengine-runner/FindApkHistory.json", str(json.dumps(ListToDictionary(findApkHistory))))  # 将历史记录的数组转换为字典并写入
            self.info.emit("操作执行完毕！")
            DisabledAndEnbled(False)
        except:
            traceback.print_exc()
            self.error.emit(title="错误", message=traceback.format_exc())
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
    QT.installRun.start()

# 安装应用
class InstallApk(QtCore.QThread):
    infor = QtCore.pyqtSignal(str)
    error = QtCore.pyqtSignal(str)
    combo = QtCore.pyqtSignal(int)

    def __init__(self, path, quit = False) -> None:
        self.path = path
        self.quit = quit
        super().__init__()

    def run(self):
        path = self.path
        quit = self.quit
        try:
            if not os.path.exists("/tmp/uengine-runner"):
                os.makedirs("/tmp/uengine-runner")
            if not os.path.exists("{}/.local/share/applications/uengine/".format(get_home())):
                print("Mkdir")
                os.makedirs("{}/.local/share/applications/uengine/".format(get_home()))
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
                if setting["SaveApk"]:
                    shutil.copy(path, "/tmp/uengine-runner/bak.apk")
            except:
                if QtWidgets.QMessageBox.critical(widget, "错误", "无法备份安装包，是否不备份安装包继续安装？\n提示：新版UEngine安装后会自动删除安装包") == QtWidgets.QMessageBox.No:
                    DisabledAndEnbled(False)
                    return
                setting["SaveApk"] = False
            print("start install apk2")
            BuildUengineDesktop(GetApkPackageName(path), GetApkActivityName(path), GetApkChineseLabel(path), iconSavePath,
                            "{}/{}.desktop".format(get_desktop_path(), GetApkPackageName(path)))
            print("start install apk3")
            BuildUengineDesktop(GetApkPackageName(path), GetApkActivityName(path), GetApkChineseLabel(path), iconSavePath,
                            "{}/.local/share/applications/uengine/{}.desktop".format(get_home(), GetApkPackageName(path)))
            commandReturn = os.system("pkexec /usr/bin/uengine-session-launch-helper -- uengine install --apk='{}'".format(path))
            try:
                if setting["SaveApk"]:
                    shutil.copy("/tmp/uengine-runner/bak.apk", path)
            except:
                self.error.emit(langFile[lang]["Main"]["MainWindow"]["Error"]["BackApkError"])
            if commandReturn != 0:
                self.error.emit("疑似 APK 安装失败，请检查 UEngine 是否正常安装、运行以及 APK 文件是否正确、完整")
                DisabledAndEnbled(False)
                return
            print("\nprint install complete")
            if quit:
                return
            self.infor.emit("操作完成！")
            findApkHistory.append(ComboInstallPath.currentText())
            self.combo.emit(0)
            write_txt(get_home() + "/.config/uengine-runner/FindApkHistory.json", str(json.dumps(ListToDictionary(findApkHistory))))  # 将历史记录的数组转换为字典并写入
        except:
            traceback.print_exc()
            self.error.emit(traceback.format_exc())
        DisabledAndEnbled(False)

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
    userChoose = {True: tk.DISABLED, False: tk.NORMAL}
    a = userChoose[choose]
    ComboInstallPath.setDisabled(choose)
    #ComboUninstallPath.configure(state=a)
    BtnFindApk.setDisabled(choose)
    BtnInstall.setDisabled(choose)
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

# 显示“提示”窗口
def helps()->"显示“提示”窗口":
    global tips
    messagebox.showinfo(title="提示", message=tips)

# 显示更新内容窗口
def UpdateThings()->"显示更新内容窗口":
    messagebox.showinfo(title="更新内容", message=updateThings)

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
        if messagebox.askokcancel(title="警告", message="删除后将无法恢复，你确定吗？\n删除后软件将会自动重启。"):
            shutil.rmtree(get_home() + "/.config/uengine-runner")
            ReStartProgram()
    except:
        traceback.print_exc()
        messagebox.showerror(title="错误", message=traceback.format_exc())

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
            if not messagebox.askokcancel(title="提示", message="桌面已经存在快捷方式，你确定要覆盖吗？"):
                DisabledAndEnbled(False)
                return
        shutil.copy(desktop, get_desktop_path())
        messagebox.showinfo(title="提示", message="发送成功！")
    except:
        traceback.print_exc()
        messagebox.showerror(title="错误", message=traceback.format_exc())
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
            if not messagebox.askokcancel(title="提示", message="启动器已经存在快捷方式，你确定要覆盖吗？"):
                DisabledAndEnbled(False)
                return
        if not os.path.exists("{}/.local/share/applications/".format(get_home())):
            os.makedirs("{}/.local/share/applications/".format(get_home()))
        shutil.copy(desktop, "{}/.local/share/applications/{}".format(get_home(), desktopName))
        os.system("chmod 755 {}/.local/share/applications/{}".format(get_home(), desktopName))
        messagebox.showinfo(title="提示", message="发送成功！")
    except:
        traceback.print_exc()
        messagebox.showerror(title="错误", message=traceback.format_exc())
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
    return GetCommandReturn("aapt dump badging '{}'".format(apkFilePath))

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

def InstallRootUengineImage():
    if not os.path.exists:
        os.mkdir("/tmp/uengine-runner")
    write_txt("/tmp/uengine-runner/install.sh", "sudo dpkg -i /tmp/uengine-runner/u*.deb\nsudo apt install -f")
    threading.Thread(target=os.system, args=[f"'{programPath}/launch.sh' deepin-terminal -C \"wget -P '/tmp/uengine-runner' 'https://hub.fastgit.xyz/gfdgd-xi/uengine-runner/releases/download/U1.2.15/uengine-android-image_1.2.15_amd64.deb' && pkexec bash '/tmp/uengine-runner/install.sh'\""]).start()

def UengineUbuntuInstall():
    threading.Thread(target=os.system, args=[f"'{programPath}/launch.sh' deepin-terminal -C \"bash '{programPath + '/uengine-installer'}'\""]).start()

def UbuntuInstallUengine():
    threading.Thread(target=os.system, args=[f"'{programPath}/launch.sh' deepin-terminal -C \"bash '{programPath + '/uengine-installer'}'\""]).start()

def BuildRootUengineImage():
    threading.Thread(target=os.system, args=[f"'{programPath}/launch.sh' deepin-terminal -C \"bash '{programPath + '/root-uengine.sh'}'\""]).start()
    
def ReinstallUengineImage():
    threading.Thread(target=os.system, args=[f"'{programPath}/launch.sh' deepin-terminal -e ''pkexec apt reinstall uengine-android-image -y"]).start()

# 生成 uengine 启动文件到桌面
def BuildUengineDesktop(packageName: "软件包名", activityName: "activity", showName: "显示名称", iconPath: "程序图标所在目录", savePath:".desktop 文件保存路径")->"生成 uengine 启动文件到桌面":
    if showName == "" or showName == None:
        showName = "未知应用"
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
'''.format(packageName, activityName, showName, iconPath, showName, showName)
    write_txt(savePath, things)

# 获取软件的中文名称
def GetApkChineseLabel(apkFilePath)->"获取软件的中文名称":
    info = GetApkInformation(apkFilePath)
    for line in info.split('\n'):
        if "application-label:" in line:
            line = line.replace("application-label:", "")
            line = line.replace("'", "")
            return line

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
        shutil.copy(programPath + "/defult.png", iconSavePath)
    except:
        traceback.print_exc()
        print("Error, show defult icon")
        shutil.copy(programPath + "/defult.png", iconSavePath)

def saveicon():
    global temppath
    global tempstr1
    iconSavePath = "{}/.local/share/icons/hicolor/256x256/apps/{}.png".format(get_home(), GetApkPackageName(temppath))
    print(iconSavePath+"iconpaths")
    SaveApkIcon(temppath, iconSavePath)

def KeyboardToMouse():
    threading.Thread(target=os.system, args=["pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY {}/uengine-keyboard".format(programPath)]).start()

# 用户自行保存APK
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
    if messagebox.askokcancel(title="警告", message="清空后数据将会完全丢失，确定要继续吗？"):
        DisabledAndEnbled(True)
        try:
            if os.path.exists("{}/.local/share/applications/uengine/".format(get_home())):
                shutil.rmtree("{}/.local/share/applications/uengine/".format(get_home()))
        except:
            traceback.print_exc()
            messagebox.showerror(title="错误", message=traceback.format_exc())
        InstallWindow.ShowWindows("pkexec rm -rfv /data/uengine")
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
    if messagebox.askyesno(title="提示", message="你没有安装Scrcpy（指使用Snap安装），\n如果你使用了其他方法安装了Scrcpy，可以输入命令“scrcpy -s '192.168.250.2:5555'”，\n是否现在要使用Snap安装Scrcpy？"):
        if not os.path.exists("/tmp/uengine-runner"):
            os.makedirs("/tmp/uengine-runner")
        write_txt("/tmp/uengine-runner/InstallScrcpy.sh", '''#!/bin/bash
sudo apt install snapd -y
sudo snap refresh
sudo snap install scrcpy''')
        threading.Thread(target=InstallWindow.ShowWindows, args=["chmod 777 /tmp/uengine-runner/InstallScrcpy.sh -Rv && pkexec /tmp/uengine-runner/InstallScrcpy.sh"]).start()
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
        result = simpledialog.askstring(title="输入apk包名", prompt="请输入要获取的apk包名以便进行下一步操作")
        if result == "" or result == None:
            return
        if os.path.exists("/data/uengine/data/data/app/{}-1".format(result)):
            break
        messagebox.showerror(title="错误", message=langFile[lang]["Main"]["MainWindow"]["Error"]["PathError"])
    path = filedialog.asksaveasfilename(title="保存apk", filetypes=[("APK 文件", "*.apk"), ("所有文件", "*.*")], initialdir=json.loads(readtxt(get_home() + "/.config/uengine-runner/SaveApk.json"))["path"])
    if path == "" or path == ():
        return
    try:
        shutil.copy("/data/uengine/data/data/app/{}-1/base.apk".format(result), path)
        write_txt(get_home() + "/.config/uengine-runner/SaveApk.json", json.dumps({"path": os.path.dirname(path)}))
        messagebox.showinfo(title="提示", message="提取完成！")
    except:
        traceback.print_exc()
        messagebox.showerror(title="错误", message=traceback.format_exc())
    
def UengineCheckCpu():
    english = GetCommandReturn("uengine check-features")
    messagebox.showinfo(title="提示", message="{}".format(english))

# 获取用户主目录
def get_home()->"获取用户主目录":
    return os.path.expanduser('~')

# 删除所有的 uengine 应用快捷方式
def CleanAllUengineDesktopLink():
    if messagebox.askokcancel(title="提示", message="你确定要删除所有的 UEngine 应用快捷方式吗？"):
        try:
            shutil.rmtree("{}/.local/share/applications/uengine".format(get_home()))
            os.makedirs("{}/.local/share/applications/uengine".format(get_home()))
            messagebox.showinfo(title="提示", message="删除完毕！")
        except:
            traceback.print_exc()
            messagebox.showerror(title="错误", message=traceback.format_exc())

# 打开 uengine 应用打包器
def OpenUengineDebBuilder():
    threading.Thread(target=os.system, args=[programPath + "/uengine-apk-builder"]).start()

# 打开 uengine 根目录
def OpenUengineRootData():
    threading.Thread(target=os.system, args=["xdg-open /data/uengine/data/data"]).start()

# 打开 uengine 用户数据目录
def OpenUengineUserData():
    threading.Thread(target=os.system, args=["xdg-open ~/安卓应用文件"]).start()

# 终端显示 adb 命令行
def AdbShellShowInTer():
    os.system("adb connect 192.168.250.2:5555")
    threading.Thread(target=os.system, args=[f"'{programPath}/launch.sh' deepin-terminal -w ~ -e 'adb -s 192.168.250.2:5555 shell'"]).start()

# 终端显示 adb top
def AdbCPUAndRAWShowInTer():
    os.system("adb connect 192.168.250.2:5555")
    threading.Thread(target=os.system, args=[f"'{programPath}/launch.sh' deepin-terminal -w ~ -e 'adb -s 192.168.250.2:5555 shell top'"]).start()

def UengineSettingShow():
    threading.Thread(target=os.system, args=["/usr/bin/uengine launch --action=android.intent.action.MAIN --package=com.android.settings --component=com.android.settings.Settings"]).start()

# 杀死 adb 进程
def AdbKillAdbProgress():
    os.system("killall adb")
    messagebox.showinfo(title="提示", message="完成！")

# 关闭 adb 服务
def AdbStopServer():
    os.system("adb kill-server")
    messagebox.showinfo(title="提示", message="完成！")

# 开启 adb 服务
def AdbStartServer():
    os.system("adb start-server")
    messagebox.showinfo(title="提示", message="完成！")

def ReinstallUengine():
    threading.Thread(target=os.system, args=[f"'{programPath}/launch.sh' deepin-terminal -C 'pkexec apt reinstall uengine uengine-android-image uengine-modules-dkms -y && notify-send -i uengine \"安装完毕！\"'"]).start()

def DelUengineCheck():
    if not os.path.exists("/usr/share/uengine/uengine-check-runnable.sh"):
        messagebox.showinfo(title="提示", message="本功能已经被删除，无法重复删除！")
        return
    if messagebox.askokcancel(title="警告", message="删除后将无法使用本软件恢复\n如果需要恢复本功能，请重新安装 UEngine！"):
        threading.Thread(target=InstallWindow.ShowWindows, args=["pkexec rm -v /usr/share/uengine/uengine-check-runnable.sh"]).start()

# 使用 adb 连接 uengine
def UengineConnectAdb():
    messagebox.showinfo(title="提示", message=subprocess.getoutput("adb connect 192.168.250.2:5555"))

# 允许用户使用 adb
def UengineUseAdb():
    # 因为需要 root，所以需要开二号程序
    os.system("adb start-server")  # 保证有生成文件
    os.system("pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY {}/uengine-useadb 0 '{}'".format(programPath, "{}/.android/adbkey.pub".format(get_home())))  # 写入配置
    if messagebox.askyesno(title="提示", message="是否要连接到 UEngine？"):
        UengineConnectAdb()

def UengineDoNotUseAdb():
    # 因为需要 root，所以需要开二号程序
    if not os.path.exists("/data/uengine/data/data/misc/adb/adb_keys"):
        messagebox.showinfo(title="提示", message="你的 uengine 在设置前已经禁用 adb 连接，无需重复设置")
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
    webbrowser.open_new_tab(programPath + "/Help/index.html")

def AllowOrDisallowUpdateAndroidApp():
    if not os.path.exists("/data/uengine/data/data/misc/adb/adb_keys"):
        if not messagebox.askyesno(title=langFile[lang]["Main"]["MainWindow"]["Answer"]["Title"], message=langFile[lang]["Main"]["MainWindow"]["Answer"]["UseAdbPackageAnswer"]):
            return
        os.system("pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY {}/uengine-useadb 0 '{}'".format(programPath,"{}/.android/adbkey.pub".format(get_home())))  # 写入配
    adb = api.Adb("192.168.250.2:5555")
    adb.Service.Close()
    adb.connect()
    if messagebox.askyesno(title=langFile[lang]["Main"]["MainWindow"]["Answer"]["Title"], message=langFile[lang]["Main"]["MainWindow"]["Answer"]["AllowOrDisallowUpdateAndroidAppAnswer"][int(adb.boolAndroidInstallOtherAppSetting())]):
        adb.setAndroidInstallOtherAppSetting(not adb.boolAndroidInstallOtherAppSetting())
        messagebox.showinfo(title=langFile[lang]["Main"]["MainWindow"]["Information"]["Title"], message=langFile[lang]["Main"]["MainWindow"]["Answer"]["CompleteInformation"])

def SetHttpProxy():
    adb = api.Adb("192.168.250.2:5555")
    adb.Service.Close()
    adb.connect()
    if not messagebox.askokcancel(title="提示", message="此功能需要安装 adb 补丁，请保证已经安装然后按下“OK”"):
        return
    proxy = easygui.enterbox(title="输入代理", msg="请输入要设置的代理（为空代表不设置代理）")
    if proxy == None:
        return
    if proxy == "":
        os.system("adb -s 192.168.250.2:5555 shell settings delete global http_proxy")
        os.system("adb -s 192.168.250.2:5555 shell settings delete global global_http_proxy_host")
        os.system("adb -s 192.168.250.2:5555 shell settings delete global global_http_proxy_port")
        messagebox.showinfo(title="提示", message="设置成功！")
    else:
        os.system(f"adb -s 192.168.250.2:5555 shell settings put global http_proxy \"{proxy}\"")
        messagebox.showinfo(title="提示", message="设置成功！")
    
    

class SettingWindow():
    saveApkOption = None
    def ShowWindow():
        setting = tk.Toplevel()
        setting.resizable(0, 0)
        setting.iconphoto(False, tk.PhotoImage(file=iconPath))
        setting.title("设置 UEngine 运行器" + version)
        saveApkFrame = ttk.LabelFrame(setting, text="Apk 安装设置")
        try:
            data = json.loads(readtxt(get_home() + "/.config/uengine-runner/setting.json"))
        except:
            messagebox.showerror(title="错误", message=langFile[lang]["Main"]["MainWindow"]["Error"]["SettingReadError"])
            setting.destroy()
        SettingWindow.saveApkOption = tk.IntVar()
        SettingWindow.saveApkOption.set(int(data["SaveApk"]))
        ttk.Radiobutton(saveApkFrame, text="不备份Apk包直接安装", value=0, variable=SettingWindow.saveApkOption).pack(anchor=tk.W)
        ttk.Radiobutton(saveApkFrame, text="备份Apk包然后在安装后自动拷贝原先目录", value=1, variable=SettingWindow.saveApkOption).pack(anchor=tk.W)
        controlFrame = ttk.Frame(setting)
        ttk.Button(controlFrame, text="取消", command=setting.destroy).grid(row=0, column=0)
        ttk.Button(controlFrame, text="保存", command=SettingWindow.SaveSetting).grid(row=0, column=1)
        saveApkFrame.pack()
        controlFrame.pack(anchor=tk.E)
    def SaveSetting():
        try:
            write_txt(get_home() + "/.config/uengine-runner/setting.json", json.dumps({"SaveApk": bool(SettingWindow.saveApkOption.get())}))
        except:
            traceback.print_exc()
            messagebox.showerror(title="错误", message=langFile[lang]["Main"]["MainWindow"]["Error"]["SettingSaveError"])
            return
        messagebox.showinfo(title="提示", message="设置保存完毕！")

class UpdateWindow():
    data = {}
    def ShowWindow():
        update = tk.Toplevel()
        update.title("检查更新")
        update.resizable(0, 0)
        update.iconphoto(False, tk.PhotoImage(file=iconPath))
        versionLabel = ttk.Label(update, text="当前版本：{}\n最新版本：未知\n更新内容：".format(version))
        updateText = tk.Text(update)
        controlFrame = ttk.Frame(update)
        ok = ttk.Button(controlFrame, text="更新（更新过程中会关闭所有Python应用，包括这个应用）", command=UpdateWindow.Update)
        cancel = ttk.Button(controlFrame, text="取消", command=update.destroy)
        try:
            UpdateWindow.data = json.loads(requests.get("http://120.25.153.144/uengine-runner/update.json").text)
            versionLabel = ttk.Label(update, text="当前版本：{}\n最新版本：{}\n更新内容：".format(version, UpdateWindow.data["Version"]))
            if UpdateWindow.data["Version"] == version:
                updateText.insert("0.0", "此为最新版本，无需更新")
                ok.configure(state=tk.DISABLED)
            else:
                updateText.insert("0.0", UpdateWindow.data["New"].replace("\\n", "\n"))
        except:
            traceback.print_exc()
            messagebox.showerror(title="错误", message=langFile[lang]["Main"]["MainWindow"]["Error"]["ConnectServerError"])
        updateText.configure(state=tk.DISABLED)
        versionLabel.pack(anchor=tk.W)
        updateText.pack()
        controlFrame.pack(anchor=tk.E)
        cancel.grid(row=0, column=0)
        ok.grid(row=0, column=1)
        update.mainloop()
    def Update():
        if not os.path.exists("/tmp/uengine-runner/update"):
            os.makedirs("/tmp/uengine-runner/update")
        try:            
            write_txt("/tmp/uengine-runner/update.sh", """#!/bin/bash
echo 删除多余的安装包
rm -rfv /tmp/uengine-runner/update/*
echo 关闭“UEngine 运行器”以及其它“Python 应用”
killall python3
echo 下载安装包
wget -P /tmp/uengine-runner/update {}
echo 安装安装包
dpkg -i /tmp/uengine-runner/update/*.deb
echo 修复依赖关系
apt install -f -y
notify-send -i uengine "更新完毕！"
zenity --info --text=\"更新完毕！\" --ellipsize
""".format(UpdateWindow.data["Url"][int(information["Package"] == "com.gitee.uengine.runner.spark")], iconPath))
        except:
            traceback.print_exc()
            easygui.textbox(title="错误", msg="更新出现错误，无法继续更新！", text=traceback.format_exc())
        os.system(f"'{programPath}/launch.sh' deepin-terminal -e pkexec bash /tmp/uengine-runner/update.sh")
        
image = None
class ApkInformation():
    def ShowWindows():
        global fullInformation
        global path
        global tab1
        path = ComboInstallPath.get()
        package = GetApkPackageName(path)
        if package == None or package == "":
            messagebox.showerror(title="错误", message=langFile[lang]["Main"]["MainWindow"]["Error"]["ApkFileError"])
            return
        message = tk.Toplevel()
        message.title("“{}“的Apk信息".format(GetApkChineseLabel(path)))
        message.iconphoto(False, tk.PhotoImage(file=iconPath))
        
        tab = ttk.Notebook(message)

        tab1 = ttk.Frame(message)
        tab2 = ttk.Frame(message)

        fullInformation = tk.Text(tab2)

        tab.add(tab1, text="简化版")
        tab.add(tab2, text="完整版")

        fullInformation.pack(expand="yes", fill="both")

        tab.pack(expand="yes", fill="both")
        
        threading.Thread(target=ApkInformation.GetInformation).start()

        message.mainloop()

    def GetInformation():
        # 获取详细信息
        fullInformation.configure(state=tk.NORMAL)
        fullInformation.insert("1.0", GetApkInformation(path))
        fullInformation.configure(state=tk.DISABLED)
        # 获取图标
        SaveApkIcon(path, "/tmp/uengine-runner-android-app-icon.png")
        # 读取图标
        global image
        image = Image.open("/tmp/uengine-runner-android-app-icon.png")
        if image.size[0] + image.size[1] <= 512:
            ttk.Label(tab1, image=ImageTk.PhotoImage(Image.open("/tmp/uengine-runner-android-app-icon.png"))).pack()
        else:
            ttk.Label(tab1, image=ImageTk.PhotoImage(Image.open("/tmp/uengine-runner-android-app-icon.png").resize((256, 256), Image.ANTIALIAS))).pack()
        image.close()
        info = '''包名：{}
中文名：{}
Activity：{}
版本：{}'''.format(GetApkPackageName(path), GetApkChineseLabel(path), GetApkActivityName(path), GetApkVersion(path))
        ttk.Label(tab1, text=info).pack()
        ttk.Button(tab1, text="查看程序评分情况", command=ApkInformation.ShowMap).pack()
        ttk.Button(tab1, text="上传程序评分情况", command=ApkInformation.UpdateMark).pack()

    def UpdateMark():
        #message = tk.Toplevel()
        #message.iconphoto(False, tk.PhotoImage(file=iconPath))
        choose = easygui.indexbox(title="选择评分", choices=["含有不良信息", "0分", "1分", "2分", "3分", "4分", "5分", "取消"], msg="""选择应用“{}”的使用评分。建议参考如下规范进行评分：
含有不良信息（-1分）：含有违法违规信息（如果有就不要选择其它选项了）
0星：完全无法使用，连安装都有问题
1星：完全无法使用，但是能正常安装
2星：可以打开，但只能使用一点点功能
3星：勉强能使用，运行也不大流畅
4星：大部分功能正常，运行流畅（可能会有点小卡）
5星：完全正常且非常流畅，没有任何功能和性能问题，就和直接在手机上用一样
""".format(GetApkChineseLabel(path)))
        print(choose)
        if choose == None or choose == 7:
            return
        try:
            messagebox.showinfo(title="提示", message=requests.post("http://120.25.153.144/uengine-runner/app/check/add.php", {"Package": GetApkPackageName(path), "Type": choose}).text)
        except:
            messagebox.showerror(title="错误", message=langFile[lang]["Main"]["MainWindow"]["Error"]["ConnectServerStarError"])


    def ShowMap():
        package = GetApkPackageName(path)
        if package == None or package == "":
            messagebox.showerror(title="错误", message=langFile[lang]["Main"]["MainWindow"]["Error"]["ApkFileError"])
            return
        try:
            data = json.loads(requests.get("http://120.25.153.144/uengine-runner/app/check/" + package +"/data.json").text)
            print(data)
        except:
            messagebox.showinfo(title="错误", message="此程序暂时没有评分，欢迎您贡献第一个评分！")
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
        matplotlib.pylab.show()

class AdbChangeUengineDisplaySize():
    def ShowWindows():
        global displayX
        global displayY
        global displaySize
        message = tk.Toplevel()
        message.iconphoto(False, tk.PhotoImage(file=iconPath))
        messageFrame = ttk.Frame(message)

        displaySize = tk.StringVar()
        displaySize.set("当前 UEngine 屏幕分辨率：正在获取")

        displaySizeLabel = ttk.Label(messageFrame, textvariable=displaySize)

        input = ttk.Frame(messageFrame)
        displayX = ttk.Entry(input)
        displayY = ttk.Entry(input)

        settingBUtton = ttk.Button(messageFrame, text="设置分辨率", command=AdbChangeUengineDisplaySize.SettingDisplaySize)

        message.title("修改 UEngine 分辨率")
        message.resizable(0, 0)
        message.iconphoto(False, tk.PhotoImage(file=iconPath))
        # get screen width and height
        screen_width = message.winfo_screenwidth()
        screen_height = message.winfo_screenheight()
        # calculate position x and y coordinates  假设主窗口大小固定 570x236像素 ，设置窗口位置为屏幕中心。 
        winwith=570
        winhigh=236
        x = (screen_width/2) - (winwith/2)
        y = (screen_height/2) - (winhigh/2)
        message.geometry("+{}+{}".format(int(x), int(y)))

        displayX.grid(row=0, column=0)
        displayY.grid(row=0, column=1)

        displaySizeLabel.grid(row=0, column=0)
        input.grid(row=1, column=0)
        settingBUtton.grid(row=2, column=0)

        messageFrame.pack()
        threading.Thread(target=AdbChangeUengineDisplaySize.GetUengineDisplaySize).start()
        message.mainloop()

    def GetUengineDisplaySize():
        global displaySize
        displaySize.set("当前 UEngine 屏幕分辨率：\n" + subprocess.getoutput("adb -s '192.168.250.2:5555' shell wm size"))
        #displaySize.set(subprocess.getoutput("adb -s '192.168.250.2:5555' shell wm size"))

    def SettingDisplaySize():
        global displayX
        global displayY
        try:
            int(displayX.get())
            int(displayY.get())
        except:
            messagebox.showerror(title="错误", message=langFile[lang]["Main"]["MainWindow"]["Error"]["InputDataError"])
            return
        os.system("adb -s '192.168.250.2:5555' shell wm size {}x{}".format(displayX.get(), displayY.get()))
        AdbChangeUengineDisplaySize.GetUengineDisplaySize()
        messagebox.showinfo(title="提示", message="执行完毕！")

# 运行命令的窗口
class InstallWindow():
    # 显示窗口
    def ShowWindows(command):
        global message
        global text
        global installTipsText
        global progressbar
        global runCommand
        message = tk.Toplevel()
        message.title("执行命令")
        message.iconphoto(False, tk.PhotoImage(file=iconPath))
        messageFrame = ttk.Frame(message)
        installTipsText = tk.StringVar()
        message.title("正在操作……")
        installTipsText.set("正在操作……")
        installTips = ttk.Label(messageFrame, textvariable=installTipsText)
        progressbar = ttk.Progressbar(messageFrame, length=500, mode='indeterminate')
        text = tk.Text(messageFrame)
        text.config(background="black", foreground="white")
        installTips.pack()
        progressbar.pack(fill="x")
        text.pack(expand='yes', fill='both')
        messageFrame.pack(expand='yes', fill='both')
        print("Run!")
        threading.Thread(target=InstallWindow.RunCommand, args=[command]).start()
        message.mainloop()
    
    # 运行命令并显示
    def RunCommand(command):
        global message
        global text
        global progressbar
        global installTipsText
        InstallWindow.AddText("$>" + command + "\n")
        progressbar.start()
        res = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # 实时读取程序返回
        while res.poll() is None:
            try:
                texts = res.stdout.readline().decode("utf8")
            except:
                texts = ""
            print(texts, end="")
            InstallWindow.AddText(texts)
        messagebox.showinfo(title="提示", message="操作完毕！")
        installTipsText.set("操作完毕！")
        message.title("操作完毕！")
        progressbar.stop()
        progressbar["value"] = 100
        # 特意添加！
        DisabledAndEnbled(False)
        if command == "pkexec rm -rfv /data/uengine":
            print("Clean!")
            if messagebox.askyesno(title="提示", message="清空完毕，将会在重启后生效，是否要重启？"):
                print("reboot")
                os.system("reboot")

    # 添加文本
    def AddText(things):
        global text
        text.configure(state=tk.NORMAL)
        text.insert("end", things)
        text.configure(state=tk.DISABLED)

class ShowTextTipsWindow():
    def ShowWindow(things):
        message = tk.Toplevel()

        message.title("提示")
        message.iconphoto(False, tk.PhotoImage(file=iconPath))

        text = tk.Text(message)
        quitButton = ttk.Button(message, text="确定", command=message.destroy)

        text.insert("end", things)
        text.configure(state=tk.DISABLED)

        text.pack(fill="both", expand="yes")
        quitButton.pack()

        message.mainloop()

# 添加/删除 uengine 应用快捷方式
class AddNewUengineDesktopLink():
    addTips = '''可以输入app的包名和Activity或通过浏览apk文件来获取包名和Activity
注意：如果是要删除只要输入包名即可'''
    def ShowWindow():
        global activityName
        global packageName
        message = tk.Toplevel()
        message.iconphoto(False, tk.PhotoImage(file=iconPath))

        tipsLabel = ttk.Label(message, text=AddNewUengineDesktopLink.addTips)
        packageName = ttk.Combobox(message, width=30)
        activityName = ttk.Combobox(message, width=30)
        findApk = ttk.Button(message, text="浏览", command=AddNewUengineDesktopLink.FindApk)
        controlFrame = ttk.Frame(message)
        testOpen = ttk.Button(controlFrame, text="打开", command=AddNewUengineDesktopLink.TestOpen)
        saveButton = ttk.Button(controlFrame, text="写入", command=AddNewUengineDesktopLink.SaveDesktopLink)
        delButton = ttk.Button(controlFrame, text="删除", command=AddNewUengineDesktopLink.DelDesktopLink)

        message.title("添加/删除 UEngine 图标")
        message.resizable(0, 0)
        message.iconphoto(False, tk.PhotoImage(file=iconPath))
        # get screen width and height
        screen_width = message.winfo_screenwidth()
        screen_height = message.winfo_screenheight()
        # calculate position x and y coordinates  假设主窗口大小固定 570x236像素 ，设置窗口位置为屏幕中心。 
        winwith=570
        winhigh=236
        x = (screen_width/2) - (winwith/2)
        y = (screen_height/2) - (winhigh/2)
        message.geometry("+{}+{}".format(int(x), int(y)))

        packageName["value"] = findApkNameHistory
        activityName["value"] = findApkActivityHistory
        
        tipsLabel.grid(row=0, column=0, columnspan=3)
        packageName.grid(row=1, column=0)
        activityName.grid(row=1, column=1)
        findApk.grid(row=1, column=2)
        controlFrame.grid(row=2, column=0, columnspan=3)
        testOpen.grid(row=0, column=0)
        saveButton.grid(row=0, column=1)
        delButton.grid(row=0, column=2)

        message.mainloop()

    # 添加快捷方式
    def SaveDesktopLink():
        try:
            if os.path.exists("{}/.local/share/applications/uengine/{}.desktop".format(get_home(), packageName.get())):
                if not messagebox.askokcancel(title="提示", message="文件已存在，确定要覆盖吗？"):
                    return
            if not os.path.exists("{}/.local/share/icons/hicolor/256x256/apps/".format(get_home())):
                os.makedirs("{}/.local/share/icons/hicolor/256x256/apps/".format(get_home()))
            global activityName
            iconSavePath = "{}/.local/share/icons/hicolor/256x256/apps/{}.png".format(get_home(), packageName.get())
            shutil.copy(programPath + "/defult.png", iconSavePath)
            BuildUengineDesktop(packageName.get(), activityName, packageName.get(), iconSavePath,
                "{}/.local/share/applications/uengine/{}.desktop".format(get_home(), packageName.get()))
            BuildUengineDesktop(packageName.get(), activityName, packageName.get(), iconSavePath,
                "{}/{}.desktop".format(get_desktop_path(), packageName.get()))
            AddNewUengineDesktopLink.SaveHistory()
            messagebox.showinfo(title="提示", message="创建完毕！")
        except:
            traceback.print_exc()
            messagebox.showerror(title="错误", message=traceback.format_exc())


    # 删除快捷方式
    def DelDesktopLink():
        try:
            global packageName
            if not os.path.exists("{}/.local/share/applications/uengine/{}.desktop".format(get_home(), packageName.get())):
                messagebox.showerror(title="错误", message="此包名对应的 UEngine 桌面快捷方式不存在！")
                return
            if not messagebox.askyesno(title="提示", message="你确定要删除吗？删除后将无法恢复！"):
                return
            try:
                os.remove("{}/.local/share/applications/uengine/{}.desktop".format(get_home(), packageName.get()))
                AddNewUengineDesktopLink.SaveHistory()
                messagebox.showinfo(title="提示", message="已删除")
            except:
                traceback.print_exc()
                messagebox.showerror(title="错误", message=traceback.format_exc())
        except:
            traceback.print_exc()
            messagebox.showerror(title="错误", message=traceback.format_exc())

    # 保存历史记录
    def SaveHistory():
        findApkNameHistory.append(packageName.get())
        findApkActivityHistory.append(activityName.get())
        packageName['value'] = findApkNameHistory
        activityName['value'] = findApkActivityHistory
        write_txt(get_home() + "/.config/uengine-runner/FindApkNameHistory.json", str(json.dumps(ListToDictionary(findApkNameHistory))))  # 将历史记录的数组转换为字典并写入 
        write_txt(get_home() + "/.config/uengine-runner/FindApkActivityHistory.json", str(json.dumps(ListToDictionary(findApkActivityHistory))))  # 将历史记录的数组转换为字典并写入

    # 打开测试
    def TestOpen():
        threading.Thread(target=os.system, args=["/usr/bin/uengine launch --package={} --component={}".format(packageName.get(), activityName.get())]).start()
        AddNewUengineDesktopLink.SaveHistory()

    # 浏览文件
    def FindApk():
        path = filedialog.askopenfilename(title="选择apk", filetypes=[("APK 文件", "*.apk"), ("所有文件", "*.*")], initialdir=json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApkName.json"))["path"])
        if path == "" or path == ():
            return
        packageName.set(GetApkPackageName(path))
        activityName.set(str(GetApkActivityName(path)))
        write_txt(get_home() + "/.config/uengine-runner/FindApkName.json", json.dumps({"path": os.path.dirname(path)}))  # 写入配置文件

def UseProgram():
    global useProgram
    useProgram = '''1、UEngine：{}
2、python3：{}
3、tkinter：{}
4、aapt：{}
5、dpkg：{}
6、mkdir：{}
7、echo
8、chmod：{}
9、adb：{}
10、deepin 终端：{}'''.format(subprocess.getoutput("uengine version"),
    subprocess.getoutput("python3 --version"),
    tk.TkVersion,
    subprocess.getoutput("aapt version"),
    subprocess.getoutput("dpkg --version"),
    subprocess.getoutput("mkdir --version"),
    subprocess.getoutput("chmod --version"),
    subprocess.getoutput("adb version"),
    subprocess.getoutput("deepin-terminal -v"))

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
aaptVersion = GetCommandReturn("aapt version")
SystemVersion = GetSystemVersion()
about = '''介绍        ：一个基于 Python3 的 tkinter 制作的 UEngine 运行器，在新版本Deepin/UOS发布后，可以在应用商店安装部分官方已适配的安卓应用，对爱好者来说，不能自己安装APK软件包始终差点意思，本程序可以为Deepin/UOS上的UEngine安卓运行环境安装自定义APK软件包，并能发送安装的APK包启动菜单到桌面或系统菜单。

版本        ：{}

适用平台    ：{}

Tk 版本     :{}

程序官网    ：{}

系统版本    : {}

©2021-{}'''.format(version, goodRunSystem, tk.TkVersion,  programUrl, SystemVersion, time.strftime("%Y"))
tips = "\n".join(information["Tips"])
updateThingsString = "\n".join(information["Update"])
title = "{} {}".format(langFile[lang]["Main"]["MainWindow"]["Title"], version)
updateTime = information["Time"]
updateThings = "{} 更新内容：\n{}\n更新时间：{}".format(version, updateThingsString, updateTime, time.strftime("%Y"))
iconPath = "{}/runner.png".format(os.path.split(os.path.realpath(__file__))[0])
desktop = programPath + "/UengineAndroidProgramList.desktop"
desktopName = "UengineAndroidProgramList.desktop"
contribute = "\n".join(information["Contribute"])
useProgram = ""
threading.Thread(target=UseProgram).start()

###########################
# 加载配置
###########################
if not os.path.exists("{}/.local/share/applications/uengine/".format(get_home())):
    os.makedirs("{}/.local/share/applications/uengine/".format(get_home()))
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
    choose = None
    choose = easygui.indexbox(msg="""在使用本程序前，请选择安装Apk包的设置以便更好的运行，下列选项的详细介绍：

不备份Apk包直接安装：适用于Deepin（旧版UEngine），安装较快，不受/tmp大小所限，但Deepin23和UOS（新版UEngine）不推荐此选项，因为安装后会自动删除Apk安装包；
备份Apk包然后在安装后自动拷贝原先目录：适用于Deepin23和UOS（新版UEngine），安装较慢，受/tmp大小所限，安装后不会丢失Apk，Deepin（旧版UEngine）不推荐使用该选项；


后期可以在程序主界面的菜单栏的“程序”=>“设置”里进行修改，
如果不知道正在使用的系统是什么版本可以打开系统设置查看。
""", title="设置", choices=["不备份Apk包直接安装", "备份Apk包然后在安装后自动拷贝原先目录"])
    if choose == None:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(title="提示", message="必须选择一个选项！否则无法进入程序！")
        sys.exit()            
    write_txt(get_home() + "/.config/uengine-runner/setting.json", json.dumps({"SaveApk": int(choose)}))


###########################
# 设置变量
###########################
findApkHistory = list(json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApkHistory.json")).values())
fineUninstallApkHistory = list(json.loads(readtxt(get_home() + "/.config/uengine-runner/FindUninstallApkHistory.json")).values())
findApkNameHistory = list(json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApkNameHistory.json")).values())
findApkActivityHistory = list(json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApkActivityHistory.json")).values())

# add sub window
#添加窗口开启关闭开关，防止重复开启
windowflag = "close"

def showhelp():
     
    #define  window and frame and button label   
    # 
    global windowflag
    if windowflag == "close":
        helpwindow=tk.Toplevel()
        helpwindow.resizable(0, 0)
        helpwindow.title("帮助")
        helpwindow.iconphoto(False, tk.PhotoImage(file=iconPath))

        # get screen width and height
        screen_width = helpwindow.winfo_screenwidth()
        screen_height = helpwindow.winfo_screenheight()
        # calculate position x and y coordinates  假设主窗口大小固定 570x236像素 ，设置窗口位置为屏幕中心。


        winwith=550
        winhigh=700
        x = (screen_width/2) - (winwith/2)
        y = (screen_height/2) - (winhigh/2)
        if not helpwindow.winfo_screenheight() > 1080:
            helpwindow.geometry(f"{winwith}x{winhigh}"+"+{:.0f}+{:.0f}".format(x, y))
     

        Frmroot=ttk.Frame(helpwindow)
        FrmMenu = ttk.Frame(Frmroot)
        FrmText = ttk.Frame(Frmroot)

        LabFrmText=ttk.LabelFrame(FrmText,text="帮助",height=800,borderwidth=3)  
        HelpStr = tk.StringVar() 
        HelpStr.set(tips)
        LabText = ttk.Label(LabFrmText, textvariable=HelpStr,width=55)
        LabText.config(wraplength=350)

        def on_closing():
            global windowflag
            windowflag = "close"
            print(windowflag)
            helpwindow.destroy()



        # define button func        
        def ChgLog():
            HelpStr.set(updateThingsString)
        def ChgAbout():
            HelpStr.set(about)
        def ChgDep():
            if useProgram == "":
                BtnZujian.configure(state=tk.DISABLED)
                return
            HelpStr.set(useProgram)
        def ChgCon():
            HelpStr.set(contribute)
        def ChgTips():
            HelpStr.set(tips)
            LabText.config(wraplength=350)
        def Egg(event):
            try:
                lists = json.loads(requests.get("http://120.25.153.144/uengine-runner/VersionList.json").text)
                data = []
                for i in lists:
                    data.append(int(requests.get("http://120.25.153.144/uengine-runner/{}/data.txt".format(i)).text))
            except:
                messagebox.showerror(title="错误", message="服务器出错！数据获取失败！")
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

        BtnReadme = ttk.Button(FrmMenu, text="使用说明",width=14,command=ChgTips)
        BtnLog = ttk.Button(FrmMenu, text="更新内容",width=14,command=ChgLog)
        BtnZujian = ttk.Button(FrmMenu, text="程序依赖的组件",width=14,command=ChgDep)
        BtnGongxian = ttk.Button(FrmMenu, text="有贡献的开发者",width=14,command=ChgCon)
        BtnAbout = ttk.Button(FrmMenu, text="关于",width=14,command=ChgAbout)
        BtnAbout.bind("<Double-Button-1>", Egg)


        #layout
        FrmMenu.grid(row=0,column=0,sticky=tk.NW)
        BtnReadme.grid(row=0,column=0,sticky=tk.NW,padx=3)
        BtnLog.grid(row=1,column=0,sticky=tk.NW,padx=3)
        BtnZujian.grid(row=2,column=0,sticky=tk.NW,padx=3)
        BtnGongxian.grid(row=3,column=0,sticky=tk.NW,padx=3)
        BtnAbout.grid(row=4,column=0,sticky=tk.NW,padx=3)

        FrmText.grid(row=0,column=1,sticky=tk.NW)
        LabFrmText.grid(row=0,column=0,sticky=tk.NW,padx=3,pady=3)
        LabText.grid(row=0,column=0,sticky=tk.NW)
      
        Frmroot.pack()
        windowflag = "open"
        print(windowflag)
        #helpwindow.mainloop()
        helpwindow.protocol("WM_DELETE_WINDOW", on_closing)
# 读取主题
try:
    theme = not ("dark" in readtxt(get_home() + "/.gtkrc-2.0") and "gtk-theme-name=" in readtxt(get_home() + "/.gtkrc-2.0"))
except:
    print("主题读取错误，默认使用浅色主题")
    theme = True
if theme:
    win = tk.Tk()
    themes = ttkthemes.ThemedStyle(win)
    themes.set_theme("breeze")
else:
    import ttkbootstrap
    style = ttkbootstrap.Style(theme="darkly")
    win = style.master  # 创建窗口
###########################
# 检查 UEngine 是否安装
###########################
if not os.path.exists("/usr/bin/uengine"):
    # 不渲染窗口
    style = ttkthemes.ThemedStyle(win)
    style.set_theme("breeze")
    win.withdraw()
    # Deepin/UOS 用户
    if "deepin" in SystemVersion.lower() or "uos" in SystemVersion.lower():
        if messagebox.askyesno(title="提示", message="您的电脑没有安装 UEngine，是否安装 UEngine 以便更好的使用\n安装完后重新启动该程序即可"):
            os.system(f"'{programPath}/launch.sh' deepin-terminal -C \"pkexec apt install uengine -y\"")
            sys.exit(0)
    # 非 Deepin/UOS 用户
    else:
        if messagebox.askyesno(title="提示", message="您的电脑没有安装 UEngine，是否安装 UEngine 以便更好的使用\n这里将会使用 shenmo 提供的脚本进行安装\n安装完后重新启动该程序即可\n提示：无法保证此安装脚本安装的 UEngine 可以使用"):
            os.system(f"'{programPath}/launch.sh' deepin-terminal -C \"bash '{programPath}/uengine-installer'\"")
            sys.exit(0)
    # 重新显示窗口
    win.wm_deiconify()

###########################
# 窗口创建
###########################
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
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
BtnUninstall = QtWidgets.QPushButton(langFile[lang]["Main"]["MainWindow"]["BtnUninstall"])
Btngeticon = QtWidgets.QPushButton(langFile[lang]["Main"]["MainWindow"]["Btngeticon"])
BtnSaveApk = QtWidgets.QPushButton(langFile[lang]["Main"]["MainWindow"]["BtnSaveApk"])
BtnApkInformation = QtWidgets.QPushButton(langFile[lang]["Main"]["MainWindow"]["BtnApkInformation"])
# 设置控件
FrmInstallWidget.setLayout(FrmInstall)
FrmInstallWidget.setSizePolicy(size)
BtnShowUengineApp.setSizePolicy(size)
ComboInstallPath.setEditable(True)
ComboInstallPath.addItems(findApkHistory)
ComboInstallPath.setFixedSize(ComboInstallPath.frameSize().width() * 5, ComboInstallPath.frameSize().height())
# 绑定信号
BtnFindApk.clicked.connect(FindApk)
BtnInstall.clicked.connect(Button3Install)
BtnShowUengineApp.clicked.connect(Button5Click)
BtnUninstall.clicked.connect(ButtonClick8)
Btngeticon.clicked.connect(SaveIconToOtherPath)
BtnSaveApk.clicked.connect(SaveInstallUengineApp)
BtnApkInformation.clicked.connect(ApkInformation.ShowWindows)
# 布局控件
widgetLayout.addWidget(LabApkPath, 0, 0, 1, 2)
widgetLayout.addWidget(ComboInstallPath, 1, 0, 1, 2)
widgetLayout.addWidget(BtnShowUengineApp, 2, 0, 1, 1)
widgetLayout.addWidget(FrmInstallWidget, 0, 2, 3, 1)
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
help = menu.addMenu(langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Name"])

cleanProgramHistory = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][0]["Menu"][0])
settingWindow = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][0]["Menu"][2])
exitProgram = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][0]["Menu"][1])
programmenu.addAction(cleanProgramHistory)
programmenu.addAction(settingWindow)
programmenu.addSeparator()
programmenu.addAction(exitProgram)
# 绑定事件
exitProgram.triggered.connect(CleanProgramHistory)
exitProgram.triggered.connect(SettingWindow.ShowWindow)
exitProgram.triggered.connect(window.close)

adbUengineConnect = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][0])
adbConnectDevice = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][2])
adbChangeUengineDisplaySize = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][3])
adbAndroidInstallAppList = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][4])
adbTop = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][5])
adbShell = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][6])
adbScrcpyConnectUengine = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][7])
adb.addAction(adbUengineConnect)
adb.addSeparator()
adbServer = adb.addMenu(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][1]["Name"])
adb.addAction(adbConnectDevice)
adb.addSeparator()
adb.addAction(adbChangeUengineDisplaySize)
adb.addAction(adbAndroidInstallAppList)
adb.addAction(adbTop)
adb.addAction(adbShell)
adb.addAction(adbScrcpyConnectUengine)
adb.addSeparator()
uengineUseAdbm = adb.addMenu(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][8]["Name"])
adbStartServer = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][1]["Menu"][0])
adbStopServer = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][1]["Menu"][1])
adbKillAdbProgress = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][1]["Menu"][2])
uengineConnectAdb = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][8]["Menu"][0])
uengineUseAdb = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][8]["Menu"][1])
uengineDoNotUseAdb = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][8]["Menu"][2])
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
uengineOpenDebBuilder = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][1])
uengineKeyboardToMouse = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][7])
uengineCheckCpu = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][8])
uengineUbuntuInstall = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][12])
uengineDeleteUengineCheck = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][9])
uengineReinstall = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][10])
uengineUbuntuInstall = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][14])
uengine.addAction(uengineAllowOrDisallowUpdateAndroidApp)
uengine.addAction(uengineSetHttpProxy)
uengine.addAction(uengineOpenDebBuilder)
uengine.addAction(uengineKeyboardToMouse)
uengine.addAction(uengineCheckCpu)
uengine.addAction(uengineUbuntuInstall)
uengineService = uengine.addMenu(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][2]["Name"])
uengineInternet = uengine.addMenu(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Name"])
uengineIcon = uengine.addMenu(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Name"])
uengine.addMenu(uengineUseAdbm)
uengineData = uengine.addMenu(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][6]["Name"])
uengine.addAction(uengineDeleteUengineCheck)
uengine.addAction(uengineReinstall)
uengineRoot = uengine.addMenu(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][11]["Name"])
uengine.addAction(uengineUbuntuInstall)
# 绑定信号
uengineAllowOrDisallowUpdateAndroidApp.triggered.connect(AllowOrDisallowUpdateAndroidApp)
uengineSetHttpProxy.triggered.connect(SetHttpProxy)
uengineOpenDebBuilder.triggered.connect(OpenUengineDebBuilder)
uengineKeyboardToMouse.triggered.connect(KeyboardToMouse)
uengineCheckCpu.triggered.connect(UengineCheckCpu)
uengineUbuntuInstall.triggered.connect(UengineUbuntuInstall)
uengineDeleteUengineCheck.triggered.connect(DelUengineCheck)
uengineReinstall.triggered.connect(ReinstallUengine)
uengineUbuntuInstall.triggered.connect(UbuntuInstallUengine)

uengineStart = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][2]["Menu"][0])
uengineStop = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][2]["Menu"][1])
uengineRestart = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][2]["Menu"][2])
uengineService.addAction(uengineStart)
uengineService.addAction(uengineStop)
uengineService.addAction(uengineRestart)
# 绑定信号
uengineStart.triggered.connect(StartUengine)
uengineStop.triggered.connect(StopUengine)
uengineRestart.triggered.connect(UengineRestart)

uengineBridgeStart = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][0])
uengineBridgeStop = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][1])
uengineBridgeRestart = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][2])
uengineBridgeReload = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][3])
uengineBridgeForceReload = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][4])
uengineInternet.addAction(uengineBridgeStart)
uengineInternet.addAction(uengineBridgeStop)
uengineInternet.addAction(uengineReinstall)
uengineInternet.addAction(uengineBridgeReload)
uengineInternet.addAction(uengineBridgeForceReload)
# 绑定信号
uengineBridgeStart.triggered.connect(UengineBridgeStart)
uengineBridgeStop.triggered.connect(UengineBridgeStop)
uengineBridgeRestart.triggered.connect(UengineBridgeRestart)
uengineBridgeReload.triggered.connect(UengineBridgeReload)
uengineBridgeForceReload.triggered.connect(UengineBridgeForceReload)

uengineSendUengineAndroidListForDesktop = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Menu"][0])
uengineSendUengineAndroidListForLauncher = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Menu"][1])
uengineAddNewUengineDesktopLink = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Menu"][2])
uengineCleanAllUengineDesktopLink = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Menu"][3])
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
uengineOpenRootData = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][6]["Menu"][0])
uengineOpenUserData = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][6]["Menu"][1])
uengineBackClean = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][6]["Menu"][2])
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

helpOpenProgramUrl = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][0])
helpUengineRunnerBugUpload = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][2])
helpShowHelp = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][4])
helpRunnerUpdate = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][3])
helpAbout = QtWidgets.QAction(langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][1])
help.addAction(helpOpenProgramUrl)
help.addAction(helpUengineRunnerBugUpload)
help.addAction(helpShowHelp)
help.addAction(helpRunnerUpdate)
help.addAction(helpAbout)
# 绑定信号
helpOpenProgramUrl.triggered.connect(OpenProgramURL)
helpUengineRunnerBugUpload.triggered.connect(UengineRunnerBugUpload)
helpShowHelp.triggered.connect(ShowHelp)
helpRunnerUpdate.triggered.connect(UpdateWindow.ShowWindow)
helpAbout.triggered.connect(showhelp)

# 设置窗口
widget.setLayout(widgetLayout)
window.setCentralWidget(widget)
window.setWindowTitle(title)
window.show()
window.setFixedSize(window.frameSize().width(), window.frameSize().height())
sys.exit(app.exec_())

# 设置窗口
#style = ttkthemes.ThemedStyle(win)
#style.set_theme("breeze")
window = ttk.Frame(win)
win.title(title)
win.resizable(0, 0)
win.iconphoto(False, tk.PhotoImage(file=iconPath))

# get screen width and height
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
# calculate position x and y coordinates  假设主窗口大小固定 570x236像素 ，设置窗口位置为屏幕中心。 
winwith=570
winhigh=236
x = (screen_width/2) - (winwith/2)
y = (screen_height/2) - (winhigh/2)

win.geometry(""+"+{:.0f}+{:.0f}".format(x, y))

# 创建控件
FrmInstall = ttk.Frame(window)
#FrmUninstall = ttk.Frame(window)
LabApkPath = ttk.Label(window, text=langFile[lang]["Main"]["MainWindow"]["LabApkPath"])
ComboInstallPath = ttk.Combobox(window, width=50)
BtnFindApk = ttk.Button(FrmInstall, text=langFile[lang]["Main"]["MainWindow"]["BtnFindApk"], command=FindApk)
BtnInstall = ttk.Button(FrmInstall, text=langFile[lang]["Main"]["MainWindow"]["BtnInstall"], command=Button3Install)
BtnShowUengineApp = ttk.Button(window, text=langFile[lang]["Main"]["MainWindow"]["BtnShowUengineApp"], command=Button5Click)
BtnUninstall = ttk.Button(FrmInstall, text=langFile[lang]["Main"]["MainWindow"]["BtnUninstall"], command=ButtonClick8)
Btngeticon = ttk.Button(FrmInstall, text=langFile[lang]["Main"]["MainWindow"]["Btngeticon"], command=SaveIconToOtherPath)
BtnSaveApk = ttk.Button(FrmInstall, text=langFile[lang]["Main"]["MainWindow"]["BtnSaveApk"], command=SaveInstallUengineApp)
BtnApkInformation = ttk.Button(FrmInstall, text=langFile[lang]["Main"]["MainWindow"]["BtnApkInformation"], command=ApkInformation.ShowWindows)
# 设置菜单栏
menu = tk.Menu(window, background="white")  

programmenu = tk.Menu(menu, tearoff=0, background="white")  # 设置“程序”菜单栏
adb = tk.Menu(menu, tearoff=0, background="white")
uengine = tk.Menu(menu, tearoff=0, background="white")
help = tk.Menu(menu, tearoff=0, background="white")  # 设置“帮助”菜单栏

adbServer = tk.Menu(adb, tearoff=0, background="white")

uengineService = tk.Menu(uengine, tearoff=0, background="white")
uengineInternet = tk.Menu(uengine, tearoff=0, background="white")
uengineIcon = tk.Menu(uengine, tearoff=0, background="white")
uengineUseAdb = tk.Menu(uengine, tearoff=0, background="white")
uengineData = tk.Menu(uengine, tearoff=0, background="white")
uengineRoot = tk.Menu(uengine, tearoff=0, background="white")

menu.add_cascade(label=langFile[lang]["Main"]["MainWindow"]["Menu"][0]["Name"], menu=programmenu)
menu.add_cascade(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Name"], menu=adb)
menu.add_cascade(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Name"], menu=uengine)
menu.add_cascade(label=langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Name"], menu=help)

programmenu.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][0]["Menu"][0], command=CleanProgramHistory)
programmenu.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][0]["Menu"][2], command=SettingWindow.ShowWindow)
programmenu.add_separator()  # 设置分界线
programmenu.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][0]["Menu"][1], command=window.quit)  # 设置“退出程序”

adb.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][0], command=UengineConnectAdb)
adb.add_separator()
adb.add_cascade(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][1]["Name"], menu=adbServer)
adb.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][2], command=AdbConnectDeviceShow)
adb.add_separator()
adb.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][3], command=AdbChangeUengineDisplaySize.ShowWindows)
adb.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][4], command=AdbAndroidInstallAppList)
adb.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][5], command=AdbCPUAndRAWShowInTer)
adb.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][6], command=AdbShellShowInTer)
adb.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][7], command=ScrcpyConnectUengine)
adb.add_separator()
adb.add_cascade(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][8]["Name"], menu=uengineUseAdb)

adbServer.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][1]["Menu"][0], command=AdbStartServer)
adbServer.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][1]["Menu"][1], command=AdbStopServer)
adbServer.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][1]["Menu"][2], command=AdbKillAdbProgress)

uengine.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][13], command=AllowOrDisallowUpdateAndroidApp)
uengine.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][15], command=SetHttpProxy)
uengine.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][1], command=OpenUengineDebBuilder)
uengine.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][7], command=KeyboardToMouse)
uengine.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][8], command=UengineCheckCpu)
uengine.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][12], command=UengineUbuntuInstall)
uengine.add_cascade(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][2]["Name"], menu=uengineService)
uengine.add_cascade(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Name"], menu=uengineInternet)
uengine.add_cascade(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Name"], menu=uengineIcon)
uengine.add_cascade(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][5]["Name"], menu=uengineUseAdb)
uengine.add_cascade(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][6]["Name"], menu=uengineData)
uengine.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][9], command=DelUengineCheck)
uengine.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][10], command=ReinstallUengine)
uengine.add_cascade(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][11]["Name"], menu=uengineRoot)
uengine.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][14], command=UbuntuInstallUengine)

help.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][0], command=OpenProgramURL)  # 设置“程序官网”项
help.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][2], command=UengineRunnerBugUpload)  # 设置“传bug”项
help.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][4], command=ShowHelp)  # 设置“更多帮助”项
help.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][3], command=UpdateWindow.ShowWindow)
help.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][3]["Menu"][1], command=showhelp)  # 设置“关于这个程序”项

uengineService.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][2]["Menu"][0], command=StartUengine)
uengineService.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][2]["Menu"][1], command=StopUengine)
uengineService.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][2]["Menu"][2], command=UengineRestart)

uengineInternet.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][0], command=UengineBridgeStart)
uengineInternet.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][1], command=UengineBridgeStop)
uengineInternet.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][2], command=UengineBridgeRestart)
uengineInternet.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][3], command=UengineBridgeReload)
uengineInternet.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][3]["Menu"][4], command=UengineBridgeForceReload)

uengineIcon.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Menu"][0], command=SendUengineAndroidListForDesktop)
uengineIcon.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Menu"][1], command=SendUengineAndroidListForLauncher)
uengineIcon.add_separator()
uengineIcon.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Menu"][2], command=AddNewUengineDesktopLink.ShowWindow)
uengineIcon.add_separator()
uengineIcon.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][4]["Menu"][3], command=CleanAllUengineDesktopLink)

uengineUseAdb.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][8]["Menu"][0], command=UengineConnectAdb)
uengineUseAdb.add_separator()
uengineUseAdb.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][8]["Menu"][1], command=UengineUseAdb)
uengineUseAdb.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][1]["Menu"][8]["Menu"][2], command=UengineDoNotUseAdb)

uengineData.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][6]["Menu"][0], command=OpenUengineRootData)
uengineData.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][6]["Menu"][1], command=OpenUengineUserData)
uengineData.add_separator()
uengineData.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][6]["Menu"][2], command=BackUengineClean)

uengineRoot.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][11]["Menu"][0], command=InstallRootUengineImage)
uengineRoot.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][11]["Menu"][1], command=BuildRootUengineImage)
uengineRoot.add_separator()
uengineRoot.add_command(label=langFile[lang]["Main"]["MainWindow"]["Menu"][2]["Menu"][11]["Menu"][2], command=ReinstallUengineImage)

menu.configure(activebackground="dodgerblue")
help.configure(activebackground="dodgerblue")
adb.configure(activebackground="dodgerblue")
uengine.configure(activebackground="dodgerblue")
programmenu.configure(activebackground="dodgerblue")
uengineService.configure(activebackground="dodgerblue")
uengineInternet.configure(activebackground="dodgerblue")
uengineIcon.configure(activebackground="dodgerblue")
uengineUseAdb.configure(activebackground="dodgerblue")
uengineData.configure(activebackground="dodgerblue")

# 设置控件
ComboInstallPath['value'] = findApkHistory
try:
    if sys.argv[1] == "-i":
        ComboInstallPath.set(sys.argv[2])
        print("Install Path: " + sys.argv[2])
    elif sys.argv[1] == "-u":
        #ComboUninstallPath.set(sys.argv[2])
        ComboInstallPath.set(sys.argv[2])
        print("Unstall Path: " + sys.argv[2])
    else:
        print("Command Format Error")
except:
    print("Not Command Or Command Format Error")
# 显示控件
win.config(menu=menu)  # 显示菜单栏



LabApkPath.grid(row=0, column=0,sticky= tk.W,padx=3)
ComboInstallPath.grid(row=1, column=0,padx=3)


FrmInstall.grid(row=0, column=1,padx=3, rowspan=3)
BtnFindApk.grid(row=0, column=0)
BtnInstall.grid(row=0, column=1)

BtnUninstall.grid(row=1, column=0)

BtnShowUengineApp.grid(row=2, column=0,sticky= tk.W,padx=3,pady=2)

BtnApkInformation.grid(row=2, column=1,sticky= tk.W,padx=3,pady=2)
Btngeticon.grid(row=1, column=1,sticky= tk.W,padx=3,pady=2)
BtnSaveApk.grid(row=2, column=0,sticky= tk.W,padx=3,pady=2)

window.pack()

win.mainloop()
