#!/usr/bin/env python3
# 使用系统默认的 python3 运行
###########################################################################################
# 作者：gfdgd xi
# 版本：1.0.0
# 更新时间：2021年
# 感谢：
# 基于 Python3 的 tkinter 构建
###########################################################################################
#################
# 引入所需的库
#################
import os
import sys
import time
import shutil
import threading
import webbrowser
import subprocess
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog

def KillAdbProgress():
    Return = GetCommandReturn("killall adb")
    if Return is "":
        Return = "OK!"
    messagebox.showinfo(title="tips", message=Return)

def Button1Click():
    if combobox2.get() is "":
        messagebox.showerror(title="Tips", message="Don't input right things in ComboBox")
        return
    DisabledAndEnbled(True)
    threading.Thread(target=ConnectPhoneIp).start()

def ConnectPhoneIp():
    messagebox.showinfo(title="tips", message=GetCommandReturn("adb connect '{}'".format(combobox2.get())))
    DisabledAndEnbled(False)

def FindApk():
    path = filedialog.askopenfilename(title="", filetypes=[("APK 文件", "*.apk"), ("所有文件", "*.*")])
    if path is not None:
        combobox1.set(path)

def Button3Install():
    if combobox1.get() is "":
        messagebox.showerror(title="Tips", message="Don't input right things in ComboBox")
        return
    DisabledAndEnbled(True)
    threading.Thread(target=InstallApk, args=(combobox1.get(),)).start()

def InstallApk(path):
    messagebox.showinfo(title="Tips", message=GetCommandReturn("adb install '{}'".format(path)))
    DisabledAndEnbled(False)

def DisabledAndEnbled(choose):
    userChoose = {True: tk.DISABLED, False: tk.NORMAL}
    a = userChoose[choose]
    combobox1.configure(state=a)
    combobox2.configure(state=a)
    button1.configure(state=a)
    button2.configure(state=a)
    button3.configure(state=a)
    button4.configure(state=a)

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
    messagebox.showinfo(title="关于这个程序", message=about)

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
    if messagebox.askokcancel(title="警告", message="删除后将无法恢复，你确定吗？\n删除后软件将会自动重启。"):
        shutil.rmtree(get_home() + "/.config/uengine-runner")
        ReStartProgram()

# 获取用户主目录
def get_home():
    return os.path.expanduser('~')

###########################
# 程序信息
###########################
programUrl = "https://gitee.com/gfdgd-xi/uengine-runner"
version = "1.0.0"
goodRunSystem = "Linux"
about = '''一个基于 Python3 的 tkinter 制作的
版本：{}
适用平台：{}
tkinter 版本：{}
程序官网：{}
©2021-{} gfdgd xi'''.format(version, goodRunSystem, tk.TkVersion, programUrl, time.strftime("%Y"))
tips = '''提示：
1、None'''
updateThingsString = ''''''
title = "wine 运行器 {}".format(version)
updateTime = "2021年"
updateThings = "{} 更新内容：\n{}\n更新时间：{}".format(version, updateThingsString, updateTime, time.strftime("%Y"))

window = tk.Tk()
window.title(title)
frame1 = ttk.Frame(window)
frame2 = ttk.Frame(window)
label1 = ttk.Label(window, text="要安装的 apk 路径：")
label2 = ttk.Label(window, text="要连接的设备的 IP：")
combobox1 = ttk.Combobox(window, width=100)
combobox2 = ttk.Combobox(window, width=100)
button1 = ttk.Button(frame1, text="连接设备", command=ConnectPhoneIp)
button2 = ttk.Button(window, text="浏览", command=FindApk)
button3 = ttk.Button(frame2, text="安装", command=Button3Install)
button4 = ttk.Button(frame1, text="Kill Adb Progress", command=KillAdbProgress)
button5 = ttk.Button(frame2, text="Open uengine Program List", command=Button5Click)
menu = tk.Menu(window)  # 设置菜单栏
programmenu = tk.Menu(menu, tearoff=0)  # 设置“程序”菜单栏
menu.add_cascade(label="程序", menu=programmenu)
programmenu.add_command(label="清空软件历史记录", command=CleanProgramHistory)
programmenu.add_separator()  # 设置分界线
programmenu.add_command(label="退出程序", command=window.quit)  # 设置“退出程序”项
help = tk.Menu(menu, tearoff=0)  # 设置“帮助”菜单栏
menu.add_cascade(label="帮助", menu=help)
help.add_command(label="程序官网", command=OpenProgramURL)  # 设置“程序官网”项
help.add_separator()
help.add_command(label="小提示", command=helps)  # 设置“小提示”项
help.add_command(label="更新内容", command=UpdateThings)  # 设置“更新内容”项
help.add_command(label="关于这个程序", command=about_this_program)  # 设置“关于这个程序”项
# 设置控件
window.config(menu=menu)  # 显示菜单栏
label1.grid(row=2, column=0)
label2.grid(row=0, column=0)
combobox1.grid(row=2, column=1)
combobox2.grid(row=0, column=1)
button1.grid(column=0, row=0)
button2.grid(row=2, column=2)
button3.grid(row=0, column=0)
button4.grid(column=1, row=0)
button5.grid(row=0, column=1)
frame1.grid(row=1, columnspa=3)
frame2.grid(row=3, columnspa=3)
window.mainloop()