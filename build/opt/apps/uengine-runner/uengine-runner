#!/usr/bin/env python3
# 使用系统默认的 python3 运行
###########################################################################################
# 作者：gfdgd xi
# 版本：1.2.2
# 更新时间：2021年5月30日
# 感谢：anbox、deepin 和 UOS
# 基于 Python3 的 tkinter 构建
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
import webbrowser
import subprocess
import ttkthemes
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import PIL.Image as Image
import PIL.ImageTk as ImageTk

# 卸载程序
def UninstallProgram(package: "apk 包名")->"卸载程序":
    try:
        global fineUninstallApkHistory
        Return = GetCommandReturn("pkexec /usr/bin/uengine-session-launch-helper -- uengine uninstall --pkg='{}'".format(package))
        if os.path.exists("{}/.local/share/applications/{}.desktop".format(get_home(), package)):
            os.remove("{}/.local/share/applications/{}.desktop".format(get_home(), package))
        if os.path.exists("{}/{}.desktop".format(get_desktop_path(), package)):
            os.remove("{}/{}.desktop".format(get_desktop_path(), package))
        fineUninstallApkHistory.append(combobox3.get())
        combobox3['value'] = fineUninstallApkHistory
        write_txt(get_home() + "/.config/uengine-runner/FindUninstallApkHistory.json", str(json.dumps(ListToDictionary(fineUninstallApkHistory))))  # 将历史记录的数组转换为字典并写入
        return Return
    except:
        traceback.print_exc()
        messagebox.showerror(title="错误", message=traceback.format_exc())

def ButtonClick7():
    path = filedialog.askopenfilename(title="选择 Apk", filetypes=[("APK 文件", "*.apk"), ("所有文件", "*.*")], initialdir=json.loads(readtxt(get_home() + "/.config/uengine-runner/FindUninstallApk.json"))["path"])
    if path != "" and path != "()":
        try:
            combobox3.set(path)
            write_txt(get_home() + "/.config/uengine-runner/FindUninstallApk.json", json.dumps({"path": os.path.dirname(path)}))  # 写入配置文件
        except:
            pass

def ButtonClick8():
    if combobox3.get() is "":
        messagebox.showerror(title="提示", message="信息没有填写完整，无法继续卸载 APK")
        return
    DisabledAndEnbled(True)
    if os.path.exists(combobox3.get()):
        path = GetApkPackageName(combobox3.get())
    else:
        path = combobox3.get()
    UninstallProgram(path)
    messagebox.showinfo(message="操作执行完毕！", title="提示")
    DisabledAndEnbled(False)

# 浏览窗口
def FindApk()->"浏览窗口":
    path = filedialog.askopenfilename(title="选择 Apk", filetypes=[("APK 文件", "*.apk"), ("所有文件", "*.*")], initialdir=json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApk.json"))["path"])
    if path != "" and path != "()":
        try:
            combobox1.set(path)
            write_txt(get_home() + "/.config/uengine-runner/FindApk.json", json.dumps({"path": os.path.dirname(path)}))  # 写入配置文件
        except:
            pass

def Button3Install():
    if combobox1.get() is "":
        messagebox.showerror(title="提示", message="信息没有填写完整，无法继续安装 APK")
        return
    DisabledAndEnbled(True)
    threading.Thread(target=InstallApk, args=(combobox1.get(),)).start()

# 安装应用
def InstallApk(path: "apk 路径", quit: "是否静默安装" = False):
    try:
        global findApkHistory
        commandReturn = GetCommandReturn("pkexec /usr/bin/uengine-session-launch-helper -- uengine install --apk='{}'".format(path))
        iconSavePath = "{}/.local/share/icons/hicolor/256x256/apps/{}.desktop".format(get_home(), GetApkPackageName(path))
        SaveApkIcon(path, iconSavePath)
        BuildUengineDesktop(GetApkPackageName(path), GetApkActivityName(path), GetApkChineseLabel(path), iconSavePath,
                            "{}/{}.desktop".format(get_desktop_path(), GetApkPackageName(path)))
        BuildUengineDesktop(GetApkPackageName(path), GetApkActivityName(path), GetApkChineseLabel(path), iconSavePath,
                            "{}/.local/share/applications/{}.desktop".format(get_home(), GetApkPackageName(path)))
        if quit:
            print(commandReturn)
            return
        messagebox.showinfo(title="提示", message="操作完成！")
        findApkHistory.append(combobox1.get())
        combobox1['value'] = findApkHistory
        write_txt(get_home() + "/.config/uengine-runner/FindApkHistory.json", str(json.dumps(ListToDictionary(findApkHistory))))  # 将历史记录的数组转换为字典并写入
    except:
        traceback.print_exc()
        messagebox.showerror(title="错误", message=traceback.format_exc())
    DisabledAndEnbled(False)

# 禁用或启动所有控件
def DisabledAndEnbled(choose: "启动或者禁用")->"禁用或启动所有控件":
    userChoose = {True: tk.DISABLED, False: tk.NORMAL}
    a = userChoose[choose]
    combobox1.configure(state=a)
    combobox3.configure(state=a)
    button2.configure(state=a)
    button3.configure(state=a)
    button5.configure(state=a)
    button7.configure(state=a)
    button8.configure(state=a)

# 需引入 subprocess
# 运行系统命令并获取返回值
def GetCommandReturn(cmd: "命令")->"运行系统命令并获取返回值":
    # cmd 是要获取输出的命令
    return subprocess.getoutput(cmd)

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
    mess.iconphoto(False, tk.PhotoImage(file=iconPath))
    img = ImageTk.PhotoImage(Image.open(iconPath))
    label1 = ttk.Label(message, image=img)
    label2 = ttk.Label(message, text=about)
    button1 = ttk.Button(message, text="确定", command=mess.withdraw)
    label1.pack()
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
    file = open(path, 'w', encoding='UTF-8')  # 设置文件对象
    file.write(things)  # 写入文本
    file.close()  # 关闭文本对象

# 显示本程序所有使用的程序
def ShowUseProgram()->"显示本程序所有使用的程序":
    global title
    global useProgram
    messagebox.showinfo(title="{} 使用的程序列表（部分）".format(title), message=useProgram)

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

# 获取图标在包内的路径
def GetApkIconInApk(apkFilePath)->"获取图标在包内的路径":
    info = GetApkInformation(apkFilePath)
    for line in info.split('\n'):
        if "application:" in line:
            line = line[line.index("icon='"): -1]
            line = line.replace("icon='", "")
            if "'" in line:
                line = line[0: line.index("'")]
            return line

# 获取 apk 文件的图标（部分程序不支持）
def SaveApkIcon(apkFilePath, iconSavePath)->"获取 apk 文件的图标（部分程序不支持）":
    zip = zipfile.ZipFile(apkFilePath)
    iconData = zip.read(GetApkIconInApk(apkFilePath))
    with open(iconSavePath, 'w+b') as saveIconFile:
        saveIconFile.write(iconData)

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

# 获取用户主目录
def get_home()->"获取用户主目录":
    return os.path.expanduser('~')

###########################
# 程序信息
###########################
programUrl = "https://gitee.com/gfdgd-xi/uengine-runner"
version = "1.2.2"
goodRunSystem = "Linux（deepin/UOS）"
aaptVersion = GetCommandReturn("aapt version")
about = '''一个基于 Python3 的 tkinter 制作的 uengine APK 安装器
版本：{}
适用平台：{}
tkinter 版本：{}
aapt 版本：{}
程序官网：{}
©2021-{} gfdgd xi'''.format(version, goodRunSystem, tk.TkVersion, aaptVersion,programUrl, time.strftime("%Y"))
tips = '''提示：
1、需要你有使用 root 权限的能力；
2、需要安装 uengine 才能使用；
3、如果报错是有关产生 .deksotp 文件有关，一般可以打开程序列表安装。
如果想要连接其他手机，请使用 1.2.0 以前的版本，可以使用 adb 连接。'''
updateThingsString = '''※1、对程序错误的显示更加人性化；
2、对 icon 的获取方式进行了升级；
3、增加了注释、删除部分冗余代码。'''
title = "uengine 运行器 {}".format(version)
updateTime = "2021年7月11日"
updateThings = "{} 更新内容：\n{}\n更新时间：{}".format(version, updateThingsString, updateTime, time.strftime("%Y"))
iconPath = "{}/icon.png".format(os.path.split(os.path.realpath(__file__))[0])
desktop = "/opt/apps/uengine-runner/UengineAndroidProgramList.desktop"
desktopName = "UengineAndroidProgramList.desktop"
useProgram = '''1、uengine（anbox）
2、Python3
3、tkinter（tkinter.tk、ttkthemes 和 tkinter.ttk）
4、aapt
……'''

###########################
# 加载配置
###########################
if not os.path.exists(get_home() + "/.config/uengine-runner"):  # 如果没有配置文件夹
    os.mkdir(get_home() + "/.config/uengine-runner")  # 创建配置文件夹
if not os.path.exists(get_home() + "/.config/uengine-runner/FindApkHistory.json"):  # 如果没有配置文件
    write_txt(get_home() + "/.config/uengine-runner/FindApkHistory.json", json.dumps({}))  # 创建配置文件
if not os.path.exists(get_home() + "/.config/uengine-runner/FindUninstallApkHistory.json"):  # 如果没有配置文件
    write_txt(get_home() + "/.config/uengine-runner/FindUninstallApkHistory.json", json.dumps({}))  # 创建配置文件
if not os.path.exists(get_home() + "/.config/uengine-runner/FindApk.json"):  # 如果没有配置文件
    write_txt(get_home() + "/.config/uengine-runner/FindApk.json", json.dumps({"path": "~"}))  # 写入（创建）一个配置文件
if not os.path.exists(get_home() + "/.config/uengine-runner/FindUninstallApk.json"):  # 如果没有配置文件
    write_txt(get_home() + "/.config/uengine-runner/FindUninstallApk.json", json.dumps({"path": "~"}))  # 写入（创建）一个配置文件

###########################
# 设置变量
###########################
findApkHistory = list(json.loads(readtxt(get_home() + "/.config/uengine-runner/FindApkHistory.json")).values())
fineUninstallApkHistory = list(json.loads(readtxt(get_home() + "/.config/uengine-runner/FindUninstallApkHistory.json")).values())

###########################
# 窗口创建
###########################
win = tk.Tk()  # 创建窗口
# 设置窗口所需的全局变量
checkButtonBool1 = tk.BooleanVar()
# 设置窗口
style = ttkthemes.ThemedStyle(win)
style.set_theme("adapta")
window = ttk.Frame(win)
win.attributes('-alpha', 0.5)
win.title(title)
win.resizable(0, 0)
win.iconphoto(False, tk.PhotoImage(file=iconPath))
# 创建控件
frame1 = ttk.Frame(window)
frame2 = ttk.Frame(window)
frame3 = ttk.Frame(window)
label1 = ttk.Label(window, text="要安装的 apk 路径：")
label3 = ttk.Label(window, text="要卸载的包名或程序对应的 APK 文件：")
combobox1 = ttk.Combobox(window, width=100)
combobox3 = ttk.Combobox(window, width=100)
button2 = ttk.Button(window, text="浏览", command=FindApk)
button3 = ttk.Button(frame2, text="安装", command=Button3Install)
button5 = ttk.Button(frame2, text="打开 uengine 应用列表", command=Button5Click)
button7 = ttk.Button(window, text="浏览", command=ButtonClick7)
button8 = ttk.Button(frame3, text="卸载", command=ButtonClick8)
# 设置菜单栏
menu = tk.Menu(window, background="white")  
programmenu = tk.Menu(menu, tearoff=0, background="white")  # 设置“程序”菜单栏
uengine = tk.Menu(menu, tearoff=0, background="white")
help = tk.Menu(menu, tearoff=0, background="white")  # 设置“帮助”菜单栏
menu.add_cascade(label="程序", menu=programmenu)
menu.add_cascade(label="uengine", menu=uengine)
menu.add_cascade(label="帮助", menu=help)
programmenu.add_command(label="清空软件历史记录", command=CleanProgramHistory)
programmenu.add_separator()  # 设置分界线
programmenu.add_command(label="退出程序", command=window.quit)  # 设置“退出程序”项
uengine.add_command(label="发送 uengine 应用列表到桌面", command=SendUengineAndroidListForDesktop)
uengine.add_command(label="发送 uengine 应用列表到启动器", command=SendUengineAndroidListForLauncher)
help.add_command(label="程序官网", command=OpenProgramURL)  # 设置“程序官网”项
help.add_separator()
help.add_command(label="小提示", command=helps)  # 设置“小提示”项
help.add_command(label="更新内容", command=UpdateThings)  # 设置“更新内容”项
help.add_command(label="这个程序使用的程序列表（部分）", command=ShowUseProgram)  # 设置“更新内容”项
help.add_command(label="关于这个程序", command=about_this_program)  # 设置“关于这个程序”项
menu.configure(activebackground="white")
help.configure(activebackground="white")
uengine.configure(activebackground="white")
programmenu.configure(activebackground="white")
# 设置控件
combobox3['value'] = fineUninstallApkHistory
combobox1['value'] = findApkHistory
# 显示控件
win.config(menu=menu)  # 显示菜单栏
label1.grid(row=2, column=0)
label3.grid(row=4, column=0)
combobox1.grid(row=2, column=1)
combobox3.grid(row=4, column=1)
button2.grid(row=2, column=2)
button3.grid(row=0, column=0)
button5.grid(row=0, column=1)
button7.grid(row=4, column=2)
button8.grid(row=0, column=1)
frame1.grid(row=1, columnspa=3)
frame2.grid(row=3, columnspa=3)
frame3.grid(row=5, columnspa=3)
window.pack()
win.mainloop()