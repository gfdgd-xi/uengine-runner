import os
import sys
import threading
#import ttkthemes
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

class AddVirtualMachine():
    def ShowWindow():
        messgae = tk.Toplevel()

        chooseImageString = tk.StringVar()
        chooseImageString.set("请选择……")

        nameTips = tk.Label(messgae, text="虚拟机名称")
        nameEntry = tk.Entry(messgae, width=50)
        memoryTips = tk.Label(messgae, text="虚拟机内存分配")
        memoryDefultValue = tk.Checkbutton(messgae, text="默认值")
        memoryValue = tk.Scale(messgae, from_=1, orient=tk.HORIZONTAL)
        chooseImageTips = tk.Label(messgae, text="选择虚拟机镜像：")
        chooseImage = tk.OptionMenu(messgae, chooseImageString, ["无"])
        quicklyFasterSpeed = tk.Checkbutton(messgae, text="启动 kvm 加速")
        tipsThings = tk.Label(messgae, text="虚拟机备注：")
        tipsThingsTips = tk.Text(messgae, height=5, width=50)
        controlFrame = tk.Frame(messgae)

        cancal = tk.Button(controlFrame ,text="取消")
        ok = tk.Button(controlFrame, text="确定")

        messgae.title("添加 Android X86 虚拟机")
        messgae.resizable(0, 0)

        memoryValue.set(33)

        cancal.grid(row=0, column=0)
        ok.grid(row=0, column=1)

        nameTips.grid(row=0, column=0)
        nameEntry.grid(row=0, column=1, columnspan=3)
        memoryTips.grid(row=1, column=0)
        memoryDefultValue.grid(row=1, column=1)
        memoryValue.grid(row=1, column=2)
        chooseImageTips.grid(row=2, column=0)
        chooseImage.grid(row=2, column=1)
        quicklyFasterSpeed.grid(row=2, column=2)
        tipsThings.grid(row=3, column=0)
        tipsThingsTips.grid(row=3, column=1, columnspan=3, rowspan=2, sticky=tk.W)
        controlFrame.grid(row=5, column=3, sticky=tk.E)
        #controlFrame.grid(row=5, column=2)

        messgae.mainloop()

class DelVirtualMachine():
    def Tips():
        if messagebox.askokcancel(title="提示", message="你确定要删除此虚拟机吗？\n删除后将无法恢复！"):
            messagebox.showinfo(title="提示", message="删除完毕！")

class AddVirtualImage():
    def ShowWindow():
        message = tk.Toplevel()

        urlImageDownloadTips = tk.Label(message, text="可下载镜像：")
        urlImageDownloadList = ttk.Treeview(message)
        addImage = tk.Button(message, text="➜")
        delImage = tk.Button(message, text="－")
        ImageTips = tk.Label(message, text="已下载镜像：")
        ImageList = ttk.Treeview(message)
        ok = tk.Button(message, text="确定")

        message.title("下载新的镜像")
        message.resizable(0, 0)

        urlImageDownloadTips.grid(row=0, column=0, sticky=tk.W)
        urlImageDownloadList.grid(row=1, column=0, rowspan=4)
        addImage.grid(row=2, column=1)
        delImage.grid(row=3, column=1)
        ImageTips.grid(row=0, column=2, sticky=tk.W)
        ImageList.grid(row=1, column=2, rowspan=4)
        ok.grid(row=5, column=2, sticky=tk.E)

        message.mainloop()

class SettingVirtualMachine():
    pass

def RunVirtualMachine():
    threading.Thread(target=os.system, args=["kvm --cdrom {} --hda {} -m {}G".format("", "", "")]).start()

window = tk.Tk()

virtualMachineList = ttk.Treeview(window)
addVirtualMachine = tk.Button(window, text="＋", command=AddVirtualMachine.ShowWindow)
delVirtualMachine = tk.Button(window, text="－", command=DelVirtualMachine.Tips)
addVirtualMachineImage = tk.Button(window, text="⊙", command=AddVirtualImage.ShowWindow)
settingVirtualMachine = tk.Button(window, text="⚙️")
runVirtualMachine = tk.Button(window, text="➜", command=RunVirtualMachine)
tipsThings = tk.Text(window, height=5, width=30)

menu = tk.Menu(window)
programMenu = tk.Menu(menu, tearoff=0)
yuanMenu = tk.Menu(menu, tearoff=0)

menu.add_cascade(label="程序", menu=programMenu)
menu.add_cascade(label="源", menu=yuanMenu)

programMenu.add_command(label="退出程序", command=sys.exit)

yuanMenu.add_command(label="更换源")
yuanMenu.add_command(label="修改默认源")

#window.configure(bg="white")
#ttkthemes.ThemedStyle(window).set_theme("ubuntu")
window.title("Android X86 Runner")
window.resizable(0, 0)
window.config(menu=menu)

runVirtualMachine.configure(foreground="green")
#tipsThings.configure(bg="white", foreground="black", state=tk.DISABLED)

virtualMachineList.grid(row=0, column=0, rowspan=3)
addVirtualMachine.grid(row=0, column=1)
delVirtualMachine.grid(row=0, column=2)
addVirtualMachineImage.grid(row=0, column=3)
settingVirtualMachine.grid(row=0, column=4)
runVirtualMachine.grid(row=0, column=5)
tipsThings.grid(row=2, column=1, columnspan=5, sticky=tk.W)

window.mainloop()