# uengine 运行器

#### 介绍

使用 Python3 的 tkinter 构建

（测试平台：UOS 家庭版）

（自己美术功底太差，图标直接用 anbox 的了）

#### 软件架构
i386 和 amd64


#### 源码安装教程

1.  安装所需依赖

```
sudo apt install python3 python3-tk git adb python3-pip
pip3 install pillow
pip3 install ttkthemes
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
uengine-runner
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

None


#### 特技

