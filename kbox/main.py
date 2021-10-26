#!/usr/bin/env python3
# 使用系统默认的 python3 运行
###########################################################################################
# 作者：gfdgd xi<3025613752@qq.com>
# 版本：1.5.2
# 更新时间：2021年10月16日（国庆了）
# 感谢：kbox 和 UOS
# 基于 Python3 的 tkinter 构建
# 更新：gfdgd xi<3025613752@qq.com>、actionchen<917981399@qq.com>
###########################################################################################
#################
# 引入所需的库
#################
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

temppath=""
def FindApk()->"浏览窗口":
    path = filedialog.askopenfilename(title="选择 Apk", filetypes=[("APK 文件", "*.apk"), ("所有文件", "*.*")], initialdir=json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApk.json"))["path"])
    global temppath    
    temppath = path
    print("apk path is find:" + path)
    if path != "" and path != "()":
        try:
            ComboInstallPath.set(path)
            write_txt(get_home() + "/.config/kbox-runner/FindApk.json", json.dumps({"path": os.path.dirname(path)}))  # 写入配置文件
        except:
            pass

# 安装应用
def InstallApk(path: "apk 路径", quit: "是否静默安装" = False):
    try:
        print("start install apk")
        global findApkHistory
        commandReturn = GetCommandReturn("pkexec android-appmgr.sh install '{}'".format(path))
        print(commandReturn)
        print("start install apk1")
        print("\nprint install complete")
        if quit:
            print(commandReturn)
            return
        messagebox.showinfo(title="提示", message="操作完成！")
        findApkHistory.append(ComboInstallPath.get())
        ComboInstallPath['value'] = findApkHistory
        write_txt(get_home() + "/.config/kbox-runner/FindApkHistory.json", str(json.dumps(ListToDictionary(findApkHistory))))  # 将历史记录的数组转换为字典并写入
    except:
        traceback.print_exc()
        messagebox.showerror(title="错误", message=traceback.format_exc())
    DisabledAndEnbled(False)


# 安装按钮事件
def Button3Install():
    if ComboInstallPath.get() is "" or not os.path.exists(ComboInstallPath.get()):
        messagebox.showerror(title="提示", message="信息没有填写完整或错误，无法继续安装 APK")
        return
    DisabledAndEnbled(True)
    threading.Thread(target=InstallApk, args=(ComboInstallPath.get(),)).start()

# 禁用或启动所有控件
def DisabledAndEnbled(choose: "启动或者禁用")->"禁用或启动所有控件":
    userChoose = {True: tk.DISABLED, False: tk.NORMAL}
    a = userChoose[choose]
    ComboInstallPath.configure(state=a)
    BtnFindApk.configure(state=a)
    BtnInstall.configure(state=a)
    BtnShowUengineApp.configure(state=a)
    LabApkPath.configure(state=a)

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
        if messagebox.askokcancel(title="警告", message="删除后将无法恢复，你确定吗？\n删除后软件将会自动重启。"):
            shutil.rmtree(get_home() + "/.config/kbox-runner")
            ReStartProgram()
    except:
        traceback.print_exc()
        messagebox.showerror(title="错误", message=traceback.format_exc())

# 获取用户主目录
def get_home()->"获取用户主目录":
    return os.path.expanduser('~')

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

# 获取用户主目录
def get_home()->"获取用户主目录":
    return os.path.expanduser('~')

def UengineRunnerBugUpload():
    threading.Thread(target=os.system, args=[programPath + "/kbox-runner-update-bug"]).start()

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

###########################
# 程序信息
###########################
programPath = os.path.split(os.path.realpath(__file__))[0]  # 返回 string
information = json.loads(readtxt(programPath + "/information.json"))
programUrl = information["Url"][0]
version = information["Version"]
goodRunSystem = information["System"]
aaptVersion = GetCommandReturn("aapt version")
SystemVersion = GetSystemVersion()
about = '''介绍        ：一个基于 Python3 的 tkinter 制作的 KBox 运行器，在新版本Deepin/UOS发布后，可以在应用商店安装部分官方已适配的安卓应用，对爱好者来说，不能自己安装APK软件包始终差点意思，本程序可以为UOS上的KBox安卓运行环境安装自定义APK软件包，并能发送安装的APK包启动菜单到桌面或系统菜单。

版本        ：{}

适用平台    ：{}

Tk 版本     :{}

程序官网    ：{}

系统版本    :{}

©2021-{}'''.format(version, goodRunSystem, tk.TkVersion,  programUrl, SystemVersion, time.strftime("%Y"))
tips = "\n".join(information["Tips"])
updateThingsString = "\n".join(information["Update"])
title = "KBox 安装器 {}".format(version)
updateTime = information["Time"]
updateThings = "{} 更新内容：\n{}\n更新时间：{}".format(version, updateThingsString, updateTime, time.strftime("%Y"))
iconPath = "{}/icon.png".format(os.path.split(os.path.realpath(__file__))[0])
desktop = programPath + "/UengineAndroidProgramList.desktop"
desktopName = "UengineAndroidProgramList.desktop"
contribute = "\n".join(information["Contribute"])

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

###########################
# 设置变量
###########################
findApkHistory = list(json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApkHistory.json")).values())
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
        def ChgCon():
            HelpStr.set(contribute)
        def ChgTips():
            HelpStr.set(tips)
            LabText.config(wraplength=350)

        BtnReadme = ttk.Button(FrmMenu, text="使用说明",width=14,command=ChgTips)
        BtnLog = ttk.Button(FrmMenu, text="更新内容",width=14,command=ChgLog)
        BtnGongxian = ttk.Button(FrmMenu, text="有贡献的开发者",width=14,command=ChgCon)
        BtnAbout = ttk.Button(FrmMenu, text="关于",width=14,command=ChgAbout)


        #layout
        FrmMenu.grid(row=0,column=0,sticky=tk.NW)
        BtnReadme.grid(row=0,column=0,sticky=tk.NW,padx=3)
        BtnLog.grid(row=1,column=0,sticky=tk.NW,padx=3)
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
LabApkPath = ttk.Label(window, text="安装 APK：")
ComboInstallPath = ttk.Combobox(window, width=50)
BtnFindApk = ttk.Button(FrmInstall, text="浏览", command=FindApk)
BtnInstall = ttk.Button(FrmInstall, text="安装", command=Button3Install)
BtnShowUengineApp = ttk.Button(window, text="打开程序列表", command=Button5Click)
# 设置菜单栏
menu = tk.Menu(window, background="white")  

programmenu = tk.Menu(menu, tearoff=0, background="white")  # 设置“程序”菜单栏
help = tk.Menu(menu, tearoff=0, background="white")  # 设置“帮助”菜单栏

menu.add_cascade(label="程序", menu=programmenu)
menu.add_cascade(label="关于", menu=help)

programmenu.add_command(label="清空软件历史记录", command=CleanProgramHistory)
programmenu.add_separator()  # 设置分界线
programmenu.add_command(label="退出程序", command=window.quit)  # 设置“退出程序”


help.add_command(label="程序官网", command=OpenProgramURL)  # 设置“程序官网”项
help.add_command(label="反馈程序问题和建议", command=UengineRunnerBugUpload)  # 设置“程序官网”项
help.add_command(label="关于", command=showhelp)  # 设置“关于这个程序”项


menu.configure(activebackground="dodgerblue")
help.configure(activebackground="dodgerblue")
programmenu.configure(activebackground="dodgerblue")

# 设置控件
#ComboUninstallPath['value'] = fineUninstallApkHistory
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


FrmInstall.grid(row=1, column=1,padx=3, rowspan=1)
BtnFindApk.grid(row=0, column=0)
BtnInstall.grid(row=0, column=1)

BtnShowUengineApp.grid(row=2, column=0,sticky= tk.W,padx=3,pady=2)

window.pack()

win.mainloop()
