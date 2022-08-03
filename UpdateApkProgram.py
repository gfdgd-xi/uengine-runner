import ttkthemes
import tkinter as tk
import tkinter.ttk as ttk
window = tk.Tk()
win = tk.Frame(window)

chooseFrame = ttk.Frame(win)
fiveStar = ttk.Radiobutton(chooseFrame, text="五星（正常安装、运行、卸载且无任何问题）")
fourStar = ttk.Radiobutton(chooseFrame, text="四星（正常安装、运行、卸载，但在运行时有小问题）")
threeStar = ttk.Radiobutton(chooseFrame, text="三星（正常安装、运行、卸载，但运行时体验不佳，很多功能有问题）")
twoStar = ttk.Radiobutton(chooseFrame, text="二星（正常安装、卸载，但运行难以使用甚至完全无法运行）")
oneStar = ttk.Radiobutton(chooseFrame, text="一星（无法正常安装、运行、卸载）")

window.mainloop()