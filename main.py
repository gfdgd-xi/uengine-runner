#!/usr/bin/env python3
# 使用系统默认的 python3 运行
###########################################################################################
# 作者：gfdgd xi
# 版本：1.2.0
# 更新时间：2021年5月30日
# 感谢：anbox、deepin 和 统信
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

def UninstallProgram(package):
    global fineUninstallApkHistory
    #setting = {True: "", False: "-k"}
    Return = GetCommandReturn("pkexec /usr/bin/uengine-session-launch-helper -- uengine uninstall --pkg='{}'".format(package))
    #Return = GetCommandReturn("adb shell pm uninstall {} {}".format(setting[cleanData], package))
    if os.path.exists("{}/.local/share/applications/{}.desktop".format(get_home(), package)):
        os.remove("{}/.local/share/applications/{}.desktop".format(get_home(), package))
    if os.path.exists("{}/{}.desktop".format(get_desktop_path(), package)):
        os.remove("{}/{}.desktop".format(get_desktop_path(), package))
    fineUninstallApkHistory.append(combobox3.get())
    combobox3['value'] = fineUninstallApkHistory
    write_txt(get_home() + "/.config/uengine-runner/FindUninstallApkHistory.json", str(json.dumps(ListToDictionary(fineUninstallApkHistory))))  # 将历史记录的数组转换为字典并写入
    return Return

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

def FindApk():
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

def InstallApk(path, quit = False):
    global findApkHistory
    '''if not AdbRun():
        if quit:
            return
        messagebox.showinfo(title="提示", message="你没有使用 adb 连接任何设备")
        DisabledAndEnbled(False)
        return'''
    #commandReturn = GetCommandReturn("adb install '{}'".format(path))
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
    DisabledAndEnbled(False)

def DisabledAndEnbled(choose):
    userChoose = {True: tk.DISABLED, False: tk.NORMAL}
    a = userChoose[choose]
    combobox1.configure(state=a)
    #combobox2.configure(state=a)
    combobox3.configure(state=a)
    #checkButton1.configure(state=a)
    #button1.configure(state=a)
    button2.configure(state=a)
    button3.configure(state=a)
    #button4.configure(state=a)
    button5.configure(state=a)
    #button6.configure(state=a)
    button7.configure(state=a)
    button8.configure(state=a)

# 需引入 subprocess
def GetCommandReturn(cmd):
    # cmd 是要获取输出的命令
    return subprocess.getoutput(cmd)

def Button5Click():
    threading.Thread(target=OpenUengineProgramList).start()

def OpenUengineProgramList():
    os.system("/usr/bin/uengine-launch.sh --package=org.anbox.appmgr --component=org.anbox.appmgr.AppViewActivity")

# 显示“关于这个程序”窗口
def about_this_program():
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
def helps():
    global tips
    messagebox.showinfo(title="提示", message=tips)

# 显示更新内容窗口
def UpdateThings():
    messagebox.showinfo(title="更新内容", message=updateThings)

# 打开程序官网
def OpenProgramURL():
    webbrowser.open_new_tab(programUrl)

# 重启本应用程序
def ReStartProgram():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def CleanProgramHistory():
    try:
        if messagebox.askokcancel(title="警告", message="删除后将无法恢复，你确定吗？\n删除后软件将会自动重启。"):
            shutil.rmtree(get_home() + "/.config/uengine-runner")
            ReStartProgram()
    except:
        traceback.print_exc()
        messagebox.showerror(title="错误", message=traceback.format_exc())

# 获取用户主目录
def get_home():
    return os.path.expanduser('~')

def SendUengineAndroidListForDesktop():
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
def get_desktop_path():
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

def SendUengineAndroidListForLauncher():
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
def ListToDictionary(list):
    dictionary = {}
    for i in range(len(list)):
        dictionary[i] = list[i]
    return dictionary

# 读取文本文档
def readtxt(path):
    f = open(path, "r")  # 设置文件对象
    str = f.read()  # 获取内容
    f.close()  # 关闭文本对象
    return str  # 返回结果

# 写入文本文档
def write_txt(path, things):
    file = open(path, 'w', encoding='UTF-8')  # 设置文件对象
    file.write(things)  # 写入文本
    file.close()  # 关闭文本对象

def ShowUseProgram():
    global title
    global useProgram
    messagebox.showinfo(title="{} 使用的程序列表（部分）".format(title), message=useProgram)

def GetApkPath(packetName):
    return GetCommandReturn("adb shell pm path {}".format(packetName)).replace("package:", "")

def GetAllPackageName():
    return GetCommandReturn("adb shell pm list packages")

def CopyFileToComputer(filePathInAndroid, filePathInComputer):
    return GetCommandReturn("adb pull '{}' '{}'".format(filePathInAndroid, filePathInComputer))

def GetApkInformation(apkFilePath):
    return GetCommandReturn("aapt dump badging '{}'".format(apkFilePath))

def GetApkActivityName(apkFilePath):
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

def GetApkPackageName(apkFilePath):
    info = GetApkInformation(apkFilePath)
    for line in info.split('\n'):
        if "package:" in line:
            #print(line.index("v"))
            #return line[:line.index("v")]
            line = line[0: line.index("versionCode='")]
            line = line.replace("package:", "")
            line = line.replace("name=", "")
            line = line.replace("'", "")
            line = line.replace(" ", "")
            return line

def BuildUengineDesktop(packageName, activityName, showName, iconPath, savePath):
    things = '''
    [Desktop Entry]
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

def GetApkChineseLabel(apkFilePath):
    info = GetApkInformation(apkFilePath)
    for line in info.split('\n'):
        if "application-label:" in line:
            line = line.replace("application-label:", "")
            line = line.replace("'", "")
            return line

def GetApkIconInApk(apkFilePath):
    info = GetApkInformation(apkFilePath)
    for line in info.split('\n'):
        if "application:" in line:
            line = line[line.index("icon='"): -1]
            line = line.replace("icon='", "")
            line = line.replace("'", "")
            return line

def SaveApkIcon(apkFilePath, iconSavePath):
    zip = zipfile.ZipFile(apkFilePath)
    iconData = zip.read(GetApkIconInApk(apkFilePath))
    with open(iconSavePath, 'w+b') as saveIconFile:
        saveIconFile.write(iconData)

# 获取用户桌面目录
def get_desktop_path():
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
def get_home():
    return os.path.expanduser('~')

###########################
# 程序信息
###########################
programUrl = "https://gitee.com/gfdgd-xi/uengine-runner"
version = "1.2.1"
goodRunSystem = "Linux"
about = '''一个基于 Python3 的 tkinter 制作的 uengine APK 安装器
版本：{}
适用平台：{}
tkinter 版本：{}
程序官网：{}
©2021-{} gfdgd xi'''.format(version, goodRunSystem, tk.TkVersion, programUrl, time.strftime("%Y"))
tips = '''提示：
1、需要你有使用 root 权限的能力；
2、需要安装 uengine 才能使用。
如果想要连接其他手机，请使用 1.2.0 以前的版本，可以使用 adb 连接。'''
updateThingsString = '''※1、进行了安装方式的修改（不使用 adb），修复原无法安装和卸载的问题；
2、进行了部分优化；
3、进行了功能缩水；
4、修复 deb 打包错误。'''
title = "uengine 运行器 {}".format(version)
updateTime = "2021年7月2日（考试结束了）"
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
#if not os.path.exists(get_home() + "/.config/uengine-runner/PhoneIp.json"):  # 如果没有配置文件
    #write_txt(get_home() + "/.config/uengine-runner/PhoneIp.json", json.dumps({}))  # 创建配置文件
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
#phoneIp = list(json.loads(readtxt(get_home() + "/.config/uengine-runner/PhoneIp.json")).values())
fineUninstallApkHistory = list(json.loads(readtxt(get_home() + "/.config/uengine-runner/FindUninstallApkHistory.json")).values())

###########################
# 判断参数
###########################
# None

###########################
# 窗口创建
###########################
win = tk.Tk()
checkButtonBool1 = tk.BooleanVar()
style = ttkthemes.ThemedStyle(win)
style.set_theme("adapta")
window = ttk.Frame(win)
win.attributes('-alpha', 0.5)
win.title(title)
win.resizable(0, 0)
win.iconphoto(False, tk.PhotoImage(file=iconPath))
frame1 = ttk.Frame(window)
frame2 = ttk.Frame(window)
frame3 = ttk.Frame(window)
label1 = ttk.Label(window, text="要安装的 apk 路径：")
#label2 = ttk.Label(window, text="要连接的设备的 IP（默认 IP 为 192.168.250.2）：")
label3 = ttk.Label(window, text="要卸载的包名或程序对应的 APK 文件：")
combobox1 = ttk.Combobox(window, width=100)
#combobox2 = ttk.Combobox(window, width=100)
combobox3 = ttk.Combobox(window, width=100)
#button1 = ttk.Button(frame1, text="连接设备", command=ConnectPhoneIp)
button2 = ttk.Button(window, text="浏览", command=FindApk)
button3 = ttk.Button(frame2, text="安装", command=Button3Install)
#button4 = ttk.Button(frame1, text="关闭 adb 软件进程", command=KillAdbProgress)
button5 = ttk.Button(frame2, text="打开 uengine 应用列表", command=Button5Click)
#button6 = ttk.Button(frame1, text="连接默认 IP", command=ConnectPhoneIpDefult)
button7 = ttk.Button(window, text="浏览", command=ButtonClick7)
button8 = ttk.Button(frame3, text="卸载", command=ButtonClick8)
#checkButton1 = ttk.Checkbutton(frame3, text="保留软件数据", variable=checkButtonBool1)
menu = tk.Menu(window, background="white")  # 设置菜单栏
programmenu = tk.Menu(menu, tearoff=0, background="white")  # 设置“程序”菜单栏
#adb = tk.Menu(menu, tearoff=0, background="white")
uengine = tk.Menu(menu, tearoff=0, background="white")
help = tk.Menu(menu, tearoff=0, background="white")  # 设置“帮助”菜单栏
menu.add_cascade(label="程序", menu=programmenu)
#menu.add_cascade(label="adb", menu=adb)
menu.add_cascade(label="uengine", menu=uengine)
menu.add_cascade(label="帮助", menu=help)
programmenu.add_command(label="清空软件历史记录", command=CleanProgramHistory)
programmenu.add_separator()  # 设置分界线
programmenu.add_command(label="退出程序", command=window.quit)  # 设置“退出程序”项
#adb.add_command(label="adb 连接的设备", command=ShowAdbConnect)
#adb.add_command(label="adb 连接的设备的所有软件包", command=ShowAdbInstallPackage)
uengine.add_command(label="发送 uengine 应用列表到桌面", command=SendUengineAndroidListForDesktop)
uengine.add_command(label="发送 uengine 应用列表到启动器", command=SendUengineAndroidListForLauncher)
help.add_command(label="程序官网", command=OpenProgramURL)  # 设置“程序官网”项
help.add_separator()
help.add_command(label="小提示", command=helps)  # 设置“小提示”项
help.add_command(label="更新内容", command=UpdateThings)  # 设置“更新内容”项
help.add_command(label="这个程序使用的程序列表（部分）", command=ShowUseProgram)  # 设置“更新内容”项
#help.add_command(label="关于 adb", command=AboutAdb)  # 设置“关于这个程序”项
help.add_command(label="关于这个程序", command=about_this_program)  # 设置“关于这个程序”项
menu.configure(activebackground="white")
help.configure(activebackground="white")
uengine.configure(activebackground="white")
#adb.configure(activebackground="white")
programmenu.configure(activebackground="white")
# 设置控件
combobox3['value'] = fineUninstallApkHistory
#combobox2['value'] = phoneIp
combobox1['value'] = findApkHistory
#
win.config(menu=menu)  # 显示菜单栏
label1.grid(row=2, column=0)
#label2.grid(row=0, column=0)
label3.grid(row=4, column=0)
combobox1.grid(row=2, column=1)
#combobox2.grid(row=0, column=1)
combobox3.grid(row=4, column=1)
#button1.grid(column=0, row=0)
button2.grid(row=2, column=2)
button3.grid(row=0, column=0)
#button4.grid(column=1, row=0)
button5.grid(row=0, column=1)
#button6.grid(row=0, column=3)
button7.grid(row=4, column=2)
button8.grid(row=0, column=1)
#checkButton1.grid(row=0, column=0)
frame1.grid(row=1, columnspa=3)
frame2.grid(row=3, columnspa=3)
frame3.grid(row=5, columnspa=3)
window.pack()
win.mainloop()

#########################################
# 废弃的代码
#########################################
'''def KillAdbProgress():
    DisabledAndEnbled(True)
    Return = GetCommandReturn("killall adb")
    if Return is "":
        Return = "进程已经杀死！"
    messagebox.showinfo(title="tips", message=Return)
    DisabledAndEnbled(False)'''

'''def Button1Click():
    if combobox2.get() is "":
        messagebox.showerror(title="提示", message="信息没有填写完整，无法继续连接 IP")
        return
    DisabledAndEnbled(True)
    threading.Thread(target=ConnectPhoneIp).start()'''

'''def ConnectPhoneIp():
    global phoneIp
    messagebox.showinfo(title="提示", message=GetCommandReturn("adb connect '{}'".format(combobox2.get())))
    phoneIp.append(combobox2.get())
    combobox2['value'] = phoneIp
    write_txt(get_home() + "/.config/uengine-runner/PhoneIp.json", str(json.dumps(ListToDictionary(phoneIp))))  # 将历史记录的数组转换为字典并写入
    DisabledAndEnbled(False)'''

'''def ConnectPhoneIpDefult(quit = False):
    global phoneIp
    Return = GetCommandReturn("adb connect '192.168.250.2'")
    if quit:
        print(Return)
        return
    messagebox.showinfo(title="提示", message=Return)
    phoneIp.append("192.168.250.2")
    combobox2['value'] = phoneIp
    write_txt(get_home() + "/.config/uengine-runner/PhoneIp.json", str(json.dumps(ListToDictionary(phoneIp))))  # 将历史记录的数组转换为字典并写入
    DisabledAndEnbled(False)'''

'''def AdbRun():
    Return = GetCommandReturn("adb devices").replace("\n", "").replace("List of devices attached", "").replace("* daemon not running; starting now at tcp:5037", "").replace("* daemon started successfully", "")
    if Return is "":
        return False
    return True'''

'''def AdbConnect():
    return GetCommandReturn("adb devices")'''

'''def ShowAdbConnect():
    messagebox.showinfo(title="提示", message=AdbConnect())'''

'''def AboutAdb():
    messagebox.showinfo(message=GetCommandReturn("adb version"), title="关于 adb")'''

'''def GetAllPackageName():
    return GetCommandReturn("adb shell pm list packages")'''

'''def ShowAdbInstallPackage():
    mess = tk.Toplevel()
    message = ttk.Frame(mess)
    mess.resizable(0, 0)
    mess.title("所有软件包")
    textbox1 = tk.Text(message, width=100)
    button1 = ttk.Button(message, text="确定", command=mess.withdraw)
    textbox1.insert("0.0", GetAllPackageName())
    textbox1.configure(state=tk.DISABLED)
    textbox1.pack()
    button1.pack(side="bottom")
    message.pack()
    mess.mainloop()'''