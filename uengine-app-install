#!/usr/bin/env python3
import os
import sys
if len(sys.argv) > 1:
    if sys.argv[1] == "--help":
        print("帮助：")
        print("uengine-app-install apk路径")
        sys.exit(0)
    sys.exit(os.system("sudo /usr/bin/uengine-session-launch-helper -- uengine install --apk='{}'".format(sys.argv[1])))
print("命令参数错误")
sys.exit(1)