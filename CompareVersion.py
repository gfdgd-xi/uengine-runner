#!/usr/bin/env python3
import sys
if len(sys.argv) <= 2:
    print("参数不足")
    exit()
# 忽略 - （别问为什么）
if "-" in sys.argv[1]:
    sys.argv[1] = sys.argv[1][:sys.argv[1].index("-")]
if "-" in sys.argv[2]:
    sys.argv[2] = sys.argv[2][:sys.argv[2].index("-")]
firstVersion = sys.argv[1].split(".")
secondVersion = sys.argv[2].split(".")
for i in range(len(firstVersion)):
    first = int(firstVersion[i])
    try:
        second = int(secondVersion[i])
    except:
        second = 0
    if first > second:
        print(f"{sys.argv[1]} > {sys.argv[2]}")
        sys.exit(0)
    if first < second:
        print(f"{sys.argv[1]} < {sys.argv[2]}")
        sys.exit(2)
print(f"{sys.argv[1]} = {sys.argv[2]}")
sys.exit(1)
