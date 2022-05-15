import os
import psutil
import string
import ttkthemes
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

class Program:
    def GetRoot():
        return os.geteuid() == 0

    def MountDisk():
        Disk.MountDisk(diskChoose.get(), "/data/uengine/安卓应用文件/media/" + name.get())

class Disk:
    def MountDisk(disk, path):
        if not os.path.exists(path):
            os.makedirs(path)
        os.system("mount \"{}\" \"{}\"".format(disk, path))

class File:
    def DiskList():
        diskList = []
        partitions = psutil.disk_partitions()
        for p in partitions:
            if not "loop" in p.device and not "boot" in p.device and not p.device in diskList:
                #print(p.device)
                diskList.append(p.device)
                #print(p.mountpoint)
        return diskList

if __name__ == "__main__":
    window = tk.Tk()
    print(File.DiskList())
    if not Program.GetRoot():
        window.withdraw()
        messagebox.showerror(title="错误", message="此程序必须在 root 下运行！")
        quit()
    if not os.path.exists("/data/uengine/安卓应用文件/media"):
        os.makedirs("/data/uengine/安卓应用文件/media")
        #window.withdraw()
        #messagebox.showerror(title="错误", message="目录不存在，无法继续操作！")
        #quit()
    window.title("挂载磁盘")
    diskList = File.DiskList()
    diskChoose = tk.StringVar()
    diskChoose.set(diskList[0])
    weight = ttk.Frame(window)
    ttk.Label(weight, text="挂载磁盘：").grid(row=0, column=0)
    ttk.OptionMenu(weight, diskChoose, diskList[0], *diskList).grid(row=0, column=1)
    ttk.Label(weight, text="挂载名称：").grid(row=1, column=0)
    name = ttk.Entry(weight)
    ttk.Button(weight, text="挂载", command=Program.MountDisk).grid(row=2, column=1)
    name.grid(row=1, column=1)
    weight.pack()
    window.mainloop()