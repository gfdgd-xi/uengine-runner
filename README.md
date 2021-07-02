# uengine 运行器 1.2.1

#### 介绍

使用 Python3 的 tkinter 构建

（测试平台：UOS 家庭版，deepin 20.2.2 待测试）

（自己美术功底太差，图标直接用 anbox 的了）

#### 软件架构
i386 和 amd64

#### 更新内容

1.2.1更新内容：

※1、进行了安装方式的修改（不使用 adb），修复原无法安装和卸载的问题；

2、进行了部分优化；

3、进行了功能缩水；

4、修复 deb 打包错误。

1.2.0更新内容：

1、支持安装自动添加快捷方式、卸载删除快捷方式；

2、支持使用包名或 APK 文件卸载程序；

3、支持查看安装的所有包名；

4、进行了部分优化


#### 源码安装教程

1.  安装所需依赖

```
sudo apt install python3 python3-tk git python3-pip aapt uengine
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
1、需要你有使用 root 权限的能力；

2、需要安装 uengine 才能使用。

如果想要连接其他手机，请使用 1.2.0 以前的版本，可以使用 adb 连接。


#### 特技

……