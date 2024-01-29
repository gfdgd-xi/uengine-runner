#!/usr/bin/env python3
import os
import sys
import json
import base64
import requests
print("""浣溪沙
一曲新词酒一杯，去年天气旧亭台。夕阳西下几时回？
无可奈何花落去，似曾相识燕归来。小园香径独徘徊。""")
print("")
print("听一支新曲喝一杯美酒，还是去年的天气旧日的亭台，西落的夕阳何时再回来？那花儿落去我也无可奈何，那归来的燕子似曾相识，在小园的花径上独自徘徊。")
print("================================")
programPath = os.path.split(os.path.realpath(__file__))[0]  # 返回 string
with open(f"{programPath}/information.json") as file:
    version = json.loads(file.read())["Version"]
print(requests.get(base64.b64decode("aHR0cDovLzEyMC4yNS4xNTMuMTQ0L3VlbmdpbmUtcnVubmVyL0luc3RhbGwucGhwP1ZlcnNpb249").decode("utf-8") + version).text)