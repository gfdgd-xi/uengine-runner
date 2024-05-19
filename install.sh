#!/bin/bash
cd `dirname $0`
echo 安装依赖包
sudo apt install ./deb/*.deb -y
echo 安装UEngine
sudo apt install uengine -y
echo 安装完成，按回车键推出，建议重启后再使用 UEngine
read