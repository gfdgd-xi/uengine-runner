#!/usr/bin/env python3
# 使用系统默认的 python3 运行
###########################################################################################
# 作者：gfdgd xi<3025613752@qq.com>
# 版本：1.4.0
# 更新时间：2021年8月26日
# 感谢：anbox、deepin 和 UOS
# 基于 Python3 的 tkinter 构建
# 更新：actionchen<917981399@qq.com>
###########################################################################################
#################
# 引入所需的库
#################
from genericpath import exists
import os
import sys
import time
import json
import shutil
import zipfile
import traceback
import threading
import ttkthemes
import webbrowser
import subprocess
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import tkinter.simpledialog as simpledialog
from getxmlimg import getsavexml
from tkinter.constants import TOP

# 卸载程序
def UninstallProgram(package: "apk 包名")->"卸载程序":
    try:
        global fineUninstallApkHistory
        Return = GetCommandReturn("pkexec /usr/bin/uengine-session-launch-helper -- uengine uninstall --pkg='{}'".format(package))
        if os.path.exists("{}/.local/share/applications/{}.desktop".format(get_home(), package)):
            os.remove("{}/.local/share/applications/{}.desktop".format(get_home(), package))
        if os.path.exists("{}/{}.desktop".format(get_desktop_path(), package)):
            os.remove("{}/{}.desktop".format(get_desktop_path(), package))
        fineUninstallApkHistory.append(ComboUninstallPath.get())
        ComboUninstallPath['value'] = fineUninstallApkHistory
        write_txt(get_home() + "/.config/uengine-runner/FindUninstallApkHistory.json", str(json.dumps(ListToDictionary(fineUninstallApkHistory))))  # 将历史记录的数组转换为字典并写入
        return Return
    except:
        traceback.print_exc()
        messagebox.showerror(title="错误", message=traceback.format_exc())

# 卸载文本框的浏览按钮事件
def BtnFindUninstallApkClk():
    path = filedialog.askopenfilename(title="选择 Apk", filetypes=[("APK 文件", "*.apk"), ("所有文件", "*.*")], initialdir=json.loads(readtxt(get_home() + "/.config/uengine-runner/FindUninstallApk.json"))["path"])
    if path != "" and path != "()":
        try:
            ComboUninstallPath.set(path)
            write_txt(get_home() + "/.config/uengine-runner/FindUninstallApk.json", json.dumps({"path": os.path.dirname(path)}))  # 写入配置文件
        except:
            pass

# 卸载按钮事件
def ButtonClick8():
    if ComboUninstallPath.get() is "":
        messagebox.showerror(title="提示", message="信息没有填写完整，无法继续卸载 APK")
        return
    DisabledAndEnbled(True)
    if os.path.exists(ComboUninstallPath.get()):
        path = GetApkPackageName(ComboUninstallPath.get())
    else:
        path = ComboUninstallPath.get()
    UninstallProgram(path)
    messagebox.showinfo(message="操作执行完毕！", title="提示")
    DisabledAndEnbled(False)

# 浏览窗口
# temp strs
temppath=""
def FindApk()->"浏览窗口":
    path = filedialog.askopenfilename(title="选择 Apk", filetypes=[("APK 文件", "*.apk"), ("所有文件", "*.*")], initialdir=json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApk.json"))["path"])
    global temppath    
    temppath = path
    print("apk path is find:" + path)
    if path != "" and path != "()":
        try:
            ComboInstallPath.set(path)
            write_txt(get_home() + "/.config/uengine-runner/FindApk.json", json.dumps({"path": os.path.dirname(path)}))  # 写入配置文件
        except:
            pass

# 安装按钮事件
def Button3Install():
    if ComboInstallPath.get() is "":
        messagebox.showerror(title="提示", message="信息没有填写完整，无法继续安装 APK")
        return
    DisabledAndEnbled(True)
    threading.Thread(target=InstallApk, args=(ComboInstallPath.get(),)).start()

# 安装应用
def InstallApk(path: "apk 路径", quit: "是否静默安装" = False):
    try:
        if not os.path.exists("{}/.local/share/applications/uengine/".format(get_home())):
            print("Mkdir")
            os.mkdir("{}/.local/share/applications/uengine/".format(get_home()))
        print("start install apk")
        global findApkHistory
        commandReturn = GetCommandReturn("pkexec /usr/bin/uengine-session-launch-helper -- uengine install --apk='{}'".format(path))
        print(commandReturn)
        print("start install apk12")
        iconSavePath = "{}/.local/share/icons/hicolor/256x256/apps/{}.png".format(get_home(), GetApkPackageName(path))
        tempstr1 = iconSavePath
        print("start install apk1")
        iconSaveDir = os.path.dirname(iconSavePath)
        if not os.path.exists(iconSaveDir):
          os.makedirs(iconSaveDir,exist_ok=True)
        SaveApkIcon(path, iconSavePath)
        print("start install apk2")
        BuildUengineDesktop(GetApkPackageName(path), GetApkActivityName(path), GetApkChineseLabel(path), iconSavePath,
                            "{}/{}.desktop".format(get_desktop_path(), GetApkPackageName(path)))
        print("start install apk3")
        BuildUengineDesktop(GetApkPackageName(path), GetApkActivityName(path), GetApkChineseLabel(path), iconSavePath,
                            "{}/.local/share/applications/uengine/{}.desktop".format(get_home(), GetApkPackageName(path)))
        print("\nprint install complete")
        if quit:
            print(commandReturn)
            return
        messagebox.showinfo(title="提示", message="操作完成！")
        findApkHistory.append(ComboInstallPath.get())
        ComboInstallPath['value'] = findApkHistory
        write_txt(get_home() + "/.config/uengine-runner/FindApkHistory.json", str(json.dumps(ListToDictionary(findApkHistory))))  # 将历史记录的数组转换为字典并写入
    except:
        traceback.print_exc()
        messagebox.showerror(title="错误", message=traceback.format_exc())
    DisabledAndEnbled(False)

# 禁用或启动所有控件
def DisabledAndEnbled(choose: "启动或者禁用")->"禁用或启动所有控件":
    userChoose = {True: tk.DISABLED, False: tk.NORMAL}
    a = userChoose[choose]
    ComboInstallPath.configure(state=a)
    ComboUninstallPath.configure(state=a)
    BtnFindApk.configure(state=a)
    BtnInstall.configure(state=a)
    BtnShowUengineApp.configure(state=a)
    BtnUninstallApkBrowser.configure(state=a)
    BtnUninstall.configure(state=a)
    Btngeticon.configure(state=a)
    BtnSaveApk.configure(state=a)

# 需引入 subprocess
# 运行系统命令并获取返回值
def GetCommandReturn(cmd: "命令")->"运行系统命令并获取返回值":
    # cmd 是要获取输出的命令
    return subprocess.getoutput(cmd)

# 打开所有窗口事件
def Button5Click():
    threading.Thread(target=OpenUengineProgramList).start()

# 打开“uengine 所有程序列表”
def OpenUengineProgramList()->"打开“uengine 所有程序列表”":
    os.system("/usr/bin/uengine-launch.sh --package=org.anbox.appmgr --component=org.anbox.appmgr.AppViewActivity")

# 显示“关于这个程序”窗口
def about_this_program()->"显示“关于这个程序”窗口":
    global about
    global title
    global iconPath
    mess = tk.Toplevel()
    message = ttk.Frame(mess)
    mess.resizable(0, 0)
    mess.title("关于 {}".format(title))
    #mess.iconphoto(False, tk.PhotoImage(file=iconPath))
    img = ImageTk.PhotoImage(Image.open(iconPath))
    LabApkPath = ttk.Label(message, image=img)
    label2 = ttk.Label(message, text=about)
    button1 = ttk.Button(message, text="确定", command=mess.withdraw)
    LabApkPath.pack()
    label2.pack()
    button1.pack(side="bottom")
    message.pack()
    mess.mainloop()

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

# 生成 uengine 启动文件到桌面
def BuildUengineDesktop(packageName: "软件包名", activityName: "activity", showName: "显示名称", iconPath: "程序图标所在目录", savePath:".desktop 文件保存路径")->"生成 uengine 启动文件到桌面":
    things = '''[Desktop Entry]
Categories=app;
Encoding=UTF-8
Exec=/usr/bin/uengine-launch.sh --action=android.intent.action.MAIN --package={} --component={}
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
        info = GetApkInformation(apkFilePath)
        for line in info.split('\n'):
            if "application:" in line:
                xmlpath = line.split(":")[-1].split()[-1].split("=")[-1].replace("'","")  
                if xmlpath.endswith('.xml'):
                        xmlsave = getsavexml()
                        print(xmlpath)
                        xmlsave.savexml(apkFilePath,xmlpath,iconSavePath)
                else:
                    zip = zipfile.ZipFile(apkFilePath)
                    iconData = zip.read(xmlpath)
                    with open(iconSavePath, 'w+b') as saveIconFile:
                        saveIconFile.write(iconData)
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
    apkPath = ComboInstallPath.get()
    if apkPath == "":
        messagebox.showerror(title="错误", message="你没有选择 apk 文件")
        return
    path = filedialog.asksaveasfilename(title="保存图标", filetypes=[("PNG 图片", "*.png"), ("所有文件", "*.*")], initialdir=json.loads(readtxt(get_home() + "/.config/uengine-runner/SaveApkIcon.json"))["path"])
    if not path == "":
        try:
            SaveApkIcon(apkPath, path)
        except:
            traceback.print_exc()
            messagebox.showerror(title="错误", message="本程序不支持保存该 apk 的图标")
            return
        write_txt(get_home() + "/.config/uengine-runner/SaveApkIcon.json", json.dumps({"path": os.path.dirname(path)}))  # 写入配置文件
        findApkHistory.append(ComboInstallPath.get())
        ComboInstallPath['value'] = findApkHistory
        write_txt(get_home() + "/.config/uengine-runner/FindApkHistory.json", str(json.dumps(ListToDictionary(findApkHistory))))  # 将历史记录的数组转换为字典并写入
        messagebox.showinfo(title="提示", message="保存成功！")

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

# 运行命令的窗口
class InstallWindow():
    # 显示窗口
    def ShowWindows(command):
        global message
        global text
        global installTipsText
        global progressbar
        message = tk.Toplevel()
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
        result = subprocess.getoutput(command)
        InstallWindow.AddText(result)
        messagebox.showinfo(title="提示", message="操作完毕！")
        installTipsText.set("操作完毕！")
        message.title("操作完毕！")
        progressbar.stop()
        progressbar["value"] = 100
        # 特意添加！
        DisabledAndEnbled(False)
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
        messagebox.showerror(title="错误", message="路径不存在，请重试！")
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
    
# 获取用户主目录
def get_home()->"获取用户主目录":
    return os.path.expanduser('~')

# 删除所有的 uengine 应用快捷方式
def CleanAllUengineDesktopLink():
    if messagebox.askokcancel(title="提示", message="你确定要删除所有的 uengine 应用快捷方式吗？"):
        try:
            shutil.rmtree("{}/.local/share/applications/uengine".format(get_home()))
            os.mkdir("{}/.local/share/applications/uengine".format(get_home()))
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

# 添加/删除 uengine 应用快捷方式
class AddNewUengineDesktopLink():
    addTips = '''可以输入app的包名和Activity或通过浏览apk文件来获取包名和Activity
注意：如果是要删除只要输入包名即可'''
    def ShowWindow():
        global activityName
        global packageName
        message = tk.Toplevel()

        tipsLabel = ttk.Label(message, text=AddNewUengineDesktopLink.addTips)
        packageName = ttk.Combobox(message, width=30)
        activityName = ttk.Combobox(message, width=30)
        findApk = ttk.Button(message, text="浏览", command=AddNewUengineDesktopLink.FindApk)
        controlFrame = ttk.Frame(message)
        testOpen = ttk.Button(controlFrame, text="打开", command=AddNewUengineDesktopLink.TestOpen)
        saveButton = ttk.Button(controlFrame, text="写入", command=AddNewUengineDesktopLink.SaveDesktopLink)
        delButton = ttk.Button(controlFrame, text="删除", command=AddNewUengineDesktopLink.DelDesktopLink)

        message.title("添加/删除 uengine 图标")
        message.resizable(0, 0)
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
        if os.path.exists("{}/.local/share/applications/uengine/{}.desktop".format(get_home(), packageName.get())):
            if not messagebox.askokcancel(title="提示", message="文件已存在，确定要覆盖吗？"):
                return
        global activityName
        iconSavePath = "{}/.local/share/icons/hicolor/256x256/apps/{}.png".format(get_home(), packageName.get())
        shutil.copy(programPath + "/defult.png", iconSavePath)
        BuildUengineDesktop(packageName.get(), activityName, packageName.get(), iconSavePath,
            "{}/.local/share/applications/uengine/{}.desktop".format(get_home(), packageName.get()))
        BuildUengineDesktop(packageName.get(), activityName, packageName.get(), iconSavePath,
            "{}/{}.desktop".format(get_desktop_path(), packageName.get()))
        AddNewUengineDesktopLink.SaveHistory()
        messagebox.showinfo(title="提示", message="创建完毕！")

    # 删除快捷方式
    def DelDesktopLink():
        global packageName
        if not os.path.exists("{}/.local/share/applications/uengine/{}.desktop".format(get_home(), packageName.get())):
            messagebox.showerror(title="错误", message="此包名对应的uengine桌面快捷方式不存在！")
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
        threading.Thread(target=os.system, args=["/usr/bin/uengine-launch.sh --package={} --component={}".format(packageName.get(), activityName.get())]).start()
        AddNewUengineDesktopLink.SaveHistory()

    # 浏览文件
    def FindApk():
        path = filedialog.askopenfilename(title="选择apk", filetypes=[("APK 文件", "*.apk"), ("所有文件", "*.*")], initialdir=json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApkName.json"))["path"])
        if path == "" or path == ():
            return
        packageName.set(GetApkPackageName(path))
        activityName.set(GetApkActivityName(path))
        write_txt(get_home() + "/.config/uengine-runner/FindApkName.json", json.dumps({"path": os.path.dirname(path)}))  # 写入配置文件

###########################
# 程序信息
###########################
programPath = os.path.split(os.path.realpath(__file__))[0]  # 返回 string
information = json.loads(readtxt(programPath + "/information.json"))
programUrl = information["Url"][0]
version = information["Version"]
goodRunSystem = information["System"]
aaptVersion = GetCommandReturn("aapt version")
about = '''    一个基于 Python3 的 tkinter 制作的 uengine APK 运行器

版本        ：{}

适用平台    ：{}

tkinter版本：{}

aapt 版本  ：{}

程序官网    ：{}

©2021-{}'''.format(version, goodRunSystem, tk.TkVersion, aaptVersion,programUrl, time.strftime("%Y"))
tips = "\n".join(information["Tips"])
updateThingsString = "\n".join(information["Update"])
title = "uengine 运行器 {}".format(version)
updateTime = information["Time"]
updateThings = "{} 更新内容：\n{}\n更新时间：{}".format(version, updateThingsString, updateTime, time.strftime("%Y"))
iconPath = "{}/icon.png".format(os.path.split(os.path.realpath(__file__))[0])
desktop = programPath + "/UengineAndroidProgramList.desktop"
desktopName = "UengineAndroidProgramList.desktop"
contribute = "\n".join(information["Contribute"])
useProgram = "\n".join(information["Use"])


###########################
# 加载配置
###########################
if not os.path.exists("{}/.local/share/applications/uengine/".format(get_home())):
    os.mkdir("{}/.local/share/applications/uengine/".format(get_home()))
if not os.path.exists(get_home() + "/.config/uengine-runner"):  # 如果没有配置文件夹
    os.mkdir(get_home() + "/.config/uengine-runner")  # 创建配置文件夹
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
        

        # get screen width and height
        screen_width = helpwindow.winfo_screenwidth()
        screen_height = helpwindow.winfo_screenheight()
        # calculate position x and y coordinates  假设主窗口大小固定 570x236像素 ，设置窗口位置为屏幕中心。
        winwith=550
        winhigh=700
        x = (screen_width/2) - (winwith/2)
        y = (screen_height/2) - (winhigh/2)
        
        helpwindow.geometry("550x700"+"+{:.0f}+{:.0f}".format(x, y))

        style = ttkthemes.ThemedStyle(helpwindow)
        style.set_theme("breeze")
        
        

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
            HelpStr.set(useProgram)
        def ChgCon():
            HelpStr.set(contribute)
        def ChgTips():
            HelpStr.set(tips)
            LabText.config(wraplength=350)

        BtnReadme = ttk.Button(FrmMenu, text="使用说明",width=14,command=ChgTips)
        BtnLog = ttk.Button(FrmMenu, text="更新内容",width=14,command=ChgLog)
        BtnZujian = ttk.Button(FrmMenu, text="程序依赖的组件",width=14,command=ChgDep)
        BtnGongxian = ttk.Button(FrmMenu, text="有贡献的开发者",width=14,command=ChgCon)
        BtnAbout = ttk.Button(FrmMenu, text="关于",width=14,command=ChgAbout)


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


###########################
# 窗口创建
###########################
win = tk.Tk()  # 创建窗口

# 设置窗口
style = ttkthemes.ThemedStyle(win)
style.set_theme("breeze")
window = ttk.Frame(win)
win.attributes('-alpha', 0.5)
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
FrmUninstall = ttk.Frame(window)
LabApkPath = ttk.Label(window, text="安装APK：")
LabUninstallPath = ttk.Label(window, text="卸载APK：")
ComboInstallPath = ttk.Combobox(window, width=50)
ComboUninstallPath = ttk.Combobox(window, width=50)
BtnFindApk = ttk.Button(FrmInstall, text="浏览", command=FindApk)
BtnInstall = ttk.Button(FrmInstall, text="安装", command=Button3Install)
BtnShowUengineApp = ttk.Button(window, text="打开 uengine 应用列表", command=Button5Click)
BtnUninstallApkBrowser = ttk.Button(FrmUninstall, text="浏览", command=BtnFindUninstallApkClk)
BtnUninstall = ttk.Button(FrmUninstall, text="卸载", command=ButtonClick8)
Btngeticon = ttk.Button(FrmInstall, text="保存图标", command=SaveIconToOtherPath)
BtnSaveApk = ttk.Button(FrmInstall, text="保存apk", command=SaveInstallUengineApp)
# 设置菜单栏
menu = tk.Menu(window, background="white")  

programmenu = tk.Menu(menu, tearoff=0, background="white")  # 设置“程序”菜单栏
uengine = tk.Menu(menu, tearoff=0, background="white")
help = tk.Menu(menu, tearoff=0, background="white")  # 设置“帮助”菜单栏

uengineService = tk.Menu(uengine)
uengineInternet = tk.Menu(uengine)
uengineIcon = tk.Menu(uengine)
uengineData = tk.Menu(uengine)

menu.add_cascade(label="程序", menu=programmenu)
menu.add_cascade(label="uengine", menu=uengine)
menu.add_cascade(label="关于", menu=help)

programmenu.add_command(label="清空软件历史记录", command=CleanProgramHistory)
programmenu.add_separator()  # 设置分界线
programmenu.add_command(label="退出程序", command=window.quit)  # 设置“退出程序”

uengine.add_command(label="uengine 应用打包", command=OpenUengineDebBuilder)
uengine.add_command(label="uengine 键盘映射", command=KeyboardToMouse)
uengine.add_cascade(label="uengine 服务", menu=uengineService)
uengine.add_cascade(label="uengine 网络桥接", menu=uengineInternet)
uengine.add_cascade(label="uengine 快捷方式", menu=uengineIcon)
uengine.add_cascade(label="uengine 数据", menu=uengineData)

help.add_command(label="程序官网", command=OpenProgramURL)  # 设置“程序官网”项
help.add_command(label="帮助", command=showhelp)  # 设置“关于这个程序”项

uengineService.add_command(label="启用 uengine 服务", command=StartUengine)
uengineService.add_command(label="关闭 uengine 服务", command=StopUengine)
uengineService.add_command(label="重启 uengine 服务", command=UengineRestart)

uengineInternet.add_command(label="启用 uengine 网络桥接", command=UengineBridgeStart)
uengineInternet.add_command(label="关闭 uengine 网络桥接", command=UengineBridgeStop)
uengineInternet.add_command(label="重启 uengine 网络桥接", command=UengineBridgeRestart)
uengineInternet.add_command(label="加载 uengine 网络桥接", command=UengineBridgeReload)
uengineInternet.add_command(label="强制加载 uengine 网络桥接", command=UengineBridgeForceReload)

uengineIcon.add_command(label="发送 uengine 应用列表到桌面", command=SendUengineAndroidListForDesktop)
uengineIcon.add_command(label="发送 uengine 应用列表到启动器", command=SendUengineAndroidListForLauncher)
uengineIcon.add_separator()
uengineIcon.add_command(label="添加/删除指定的 uengine 快捷方式", command=AddNewUengineDesktopLink.ShowWindow)
uengineIcon.add_separator()
uengineIcon.add_command(label="清空所有 uengine 快捷方式", command=CleanAllUengineDesktopLink)

uengineData.add_command(label="打开 uengine 根目录", command=OpenUengineRootData)
uengineData.add_command(label="打开 uengine 用户数据目录", command=OpenUengineUserData)
uengineData.add_separator()
uengineData.add_command(label="清空 uengine 数据", command=BackUengineClean)

menu.configure(activebackground="dodgerblue")
help.configure(activebackground="dodgerblue")
uengine.configure(activebackground="dodgerblue")
programmenu.configure(activebackground="dodgerblue")
uengineService.configure(activebackground="dodgerblue")
uengineInternet.configure(activebackground="dodgerblue")
uengineIcon.configure(activebackground="dodgerblue")

# 设置控件
ComboUninstallPath['value'] = fineUninstallApkHistory
ComboInstallPath['value'] = findApkHistory
try:
    if sys.argv[1] == "-i":
        ComboInstallPath.set(sys.argv[2])
        print("Install Path: " + sys.argv[2])
    elif sys.argv[1] == "-u":
        ComboUninstallPath.set(sys.argv[2])
        print("Unstall Path: " + sys.argv[2])
    else:
        print("Command Format Error")
except:
    print("Not Command Or Command Format Error")
# 显示控件
win.config(menu=menu)  # 显示菜单栏



LabApkPath.grid(row=1, column=0,sticky= tk.W,padx=3)
ComboInstallPath.grid(row=2, column=0,padx=3)


FrmInstall.grid(row=2, column=1,padx=3, rowspan=2)
BtnFindApk.grid(row=0, column=0)
BtnInstall.grid(row=0, column=1)

LabUninstallPath.grid(row=4, column=0,sticky= tk.W,padx=3)
ComboUninstallPath.grid(row=5, column=0,padx=3)

FrmUninstall.grid(row=5, column=1,padx=3)
BtnUninstallApkBrowser.grid(row=0, column=0)
BtnUninstall.grid(row=0, column=1)

BtnShowUengineApp.grid(row=6, column=0,sticky= tk.W,padx=3,pady=2)

Btngeticon.grid(row=1, column=0,sticky= tk.W,padx=3,pady=2)
BtnSaveApk.grid(row=1, column=1,sticky= tk.W,padx=3,pady=2)

window.pack()

win.mainloop()
