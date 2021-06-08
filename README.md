# uengine 运行器 1.2.0

#### 介绍

使用 Python3 的 tkinter 构建

（测试平台：UOS 家庭版）

（自己美术功底太差，图标直接用 anbox 的了）

#### 软件架构
i386 和 amd64

#### 更新内容

1.2.0更新内容：
1、支持安装自动添加快捷方式、卸载删除快捷方式；
2、支持使用包名或 APK 文件卸载程序；
3、支持查看安装的所有包名；
4、进行了部分优化


#### 源码安装教程

1.  安装所需依赖

```
sudo apt install python3 python3-tk git adb python3-pip aapt
pip3 install pillow
pip3 install ttkthemes
pip3 install pillow -U
pip3 install ttkthemes -U
```

2.  下载本程序

```
git clone https://gitee.com/gfdgd-xi/uengine-runner.git
```

3.  运行本程序

```
sudo cp uengine-runner /opt/apps -rv
chmod 777 /opt/apps/uengine-runner/main.py
sudo cp /opt/apps/uengine-runner/main.py /usr/bin/uengine-runner
./main.py
```

4.  卸载本程序
```
sudo rm /usr/bin/uengine-runner -v
sudo rm /opt/apps/uengine-runner/ -rfv
pip3 uninstall pillow
pip3 uninstall ttkthemes
```

#### 使用说明

提示：
1、先连接设备再进行操作

2、支持连接其他 Android 系统操作（需要进行设置）


#### 特技

……