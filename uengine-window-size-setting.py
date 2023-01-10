#!/usr/bin/env python3
import os
import sys
import shutil
import traceback
import updatekiller

def Add():
    try:
        shutil.copy(f"/tmp/{sys.argv[2]}.txt", f"/usr/share/uengine/appetc/{sys.argv[2]}.txt")
    except:
        traceback.print_exc()
        sys.exit(1)

def Del():
    try:
        os.remove(f"/usr/share/uengine/appetc/{sys.argv[2]}.txt")
    except:
        traceback.print_exc()
        sys.exit(1)

def Help():
    print("帮助：")
    print("-?/--help  查看程序帮助")
    print("-a/--add   设置程序显示配置（参数后面要加包名，配置需要先保存到 /tmp 下，文件名为“APK包名.txt”，需要 Root 权限）")
    print("-d/--del   删除程序显示配置（参数后面要加包名，需要 Root 权限）")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("至少要三个参数，输入 --help 获取帮助")
        sys.exit(0)
    if "-?" in sys.argv[1] or "--help" in sys.argv:
        Help()
        sys.exit(0)
    if os.geteuid() != 0:
        print("不是以 root 权限运行本程序！")
        sys.exit(1)
    if sys.argv[1] == "-a" or sys.argv[1] == "--add":
        Add()
        sys.exit(0)
    if sys.argv[1] == "-d" or sys.argv[1] == "--del":
        Del()
        sys.exit(0)
    print("参数错误！")
    sys.exit(1)
