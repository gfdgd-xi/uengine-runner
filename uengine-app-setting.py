#!/usr/bin/env python3
from modulefinder import packagePathMap
import sys
import ttkthemes
import updatekiller
import tkinter as tk
import tkinter.ttk as ttk

def main():
    window = tk.Tk()
    ttk.Label(window, text="程序包名：").grid(row=0, column=0)
    packageName = ttk.Combobox(window)
    packageName.grid(row=0, column=1)
    settingFrame = ttk.Frame(window)
    readButton = ttk.Button(window, text="确定").grid(row=0, column=2)
    settingFrame.grid(row=1, column=0, columnspan=3)
    hScreenSize = ttk.Labelframe(settingFrame, text="竖屏默认分辨率")
    vScreenSize = ttk.Labelframe(settingFrame, text="横屏默认分辨率")
    hScreenSizeWidthValue = ttk.Entry(hScreenSize)
    hScreenSizeHeightValue = ttk.Entry(hScreenSize)
    hScreenSizeWidthValue.grid(row=0, column=0)
    ttk.Label(hScreenSize, text="×").grid(row=0, column=1)
    hScreenSizeHeightValue.grid(row=0, column=2)
    vScreenSizeWidthValue = ttk.Entry(vScreenSize)
    vScreenSizeHeightValue = ttk.Entry(vScreenSize)
    vScreenSizeWidthValue.grid(row=0, column=0)
    ttk.Label(vScreenSize, text="×").grid(row=0, column=1)
    vScreenSizeHeightValue.grid(row=0, column=2)
    hScreenSize.grid(row=0, column=0)
    vScreenSize.grid(row=1, column=0)
    window.mainloop()
    return 0

if __name__ == "__main__":
    sys.exit(main())
