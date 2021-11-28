# uengine 运行器 1.5.1

### 介绍
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;新版本Deepin/UOS发布后，可以在应用商店安装部分官方已适配的安卓应用，对爱好者来说，不能自己安装APK软件包始终差点意思，本程序可以为Deepin/UOS上的UEngine安卓运行环境安装自定义APK软件包，并能发送安装的APK包启动菜单到桌面或系统菜单。  
![1.5.2](https://storage.deepin.org/thread/202111281607295590_截图_选择区域_20211128160706.png)
（测试平台：UOS 家庭版，deepin 20.2.2,UOS 专业版 1040）   
（自己美术功底太差，图标直接用 anbox 的了）   

### 更新内容
#### V1.5.2（2021-11-28）：
**※1、支持安装和构建带 Root 的 UEngine 的镜像**  
2、更新了反馈链接  
![](https://storage.deepin.org/thread/202111281607295590_截图_选择区域_20211128160706.png)  

#### V1.5.1（2021-10-05，国庆节版）：
**※1、精简用户界面，合并安装和卸载输入框和浏览按钮等**  
**※2、修复安装以其的程序图标无法点击进入的问题（deepin 社区版不存在此问题）**  
**※3、支持在程序本体反馈问题**  
4、修复了菜单栏的部分显示问题  
5、支持显示 apk 的部分信息  
6、支持删除 UEngine 程序运行检查以及重新安装 UEngine 的功能  
7、自带有跳过家庭版必须有指定包名才能运行程序限制的脚本  
8、补回依赖包“adb”  
![1.5.1](https://storage.deepin.org/thread/202110051821076836_截图_dde-desktop_20211005182021.png)

#### V1.5.0（2021-09-21，中秋节版）：
**没有什么实质性的功能，只是开始有多语言支持**  
**※1、部分窗口支持英语**  
2、修复在英语状态下启动器图标名称异常的问题   
![1.5.0](https://storage.deepin.org/thread/202109202157289430_截图_选择区域_20210920215550.png)

#### V1.4.3（2021-09-11，开学第一版）：
**※1、支持打包器打包的包名带前缀“uengine-dc”**  
**※2、修复了两种情况可能导致程序卡住/出错无法继续运行的情况（配置文件夹不齐全和获取版本信息卡住两种情况）**  
**※3、修改了 UEngine 打包器打包的应用包名可能有大写的情况**  
4、支持一键使用 Scrcpy 连接 UEngine（①先安装 adb 破解补丁；②请确保是使用snap安装的 Scrcpy【目前只支持 snap 安装的 Scrcpy 进行连接】）  
5、支持右键打包 apk  
![1.4.3](https://storage.deepin.org/thread/202109111635389828_截图_选择区域_20210911163449.png)

#### V1.4.2（2021-08-30，快开学了）：
**※1、添加adb破解补丁（用于可以让adb连接UEngine）并支持adb的部分操作;**  
2、菜单栏的项目添加以及外观优化;  
3、修复键盘映射无法添加新映射的问题并修改键盘映射启动方式;  
4、把 uengine 改为 UEngine;  
5、修改 pkexec 获取密码时显示的图标和文本;  
6、添加了 UEngine 系统设置的快捷方式;  
![1.4.2](https://storage.deepin.org/thread/202108301750554993_截图_选择区域_20210830134502.png)

#### V1.4.1（2021-08-26）：
**※1、初步支持键盘映射**  
2、修复新版包在发送uengine列表快捷方式时会提示找不到文件  
![1.4.1](https://storage.deepin.org/thread/20210826151947783_截图_选择区域_20210826151312.png)

#### V1.4.0（2021-08-19）：
**※1、添加新版打包方式（deepin打包方式）;**  
**※2、支持测试运行/创建/删除uengine图标;**  
**※3、支持提取安装的apk;**  
**※4、支持打包deb包;**  
5、修改菜单栏布局;  
6、支持打开uengine数据目录和用户数据目录;  
7、程序信息保存到json,非直接写入程序本体;  
8、更多命令操作;  
![1.4.0](https://storage.deepin.org/thread/202108191410327464_截图_选择区域_20210819140938.png)

#### V1.3.2（2021-08-16）：
**※1、支持uengine数据重置;**  
**※2、支持修改uengine网络桥接的启动状态;**  
**※3、支持右键安装/卸载;**  
**※4、支持启用或禁用uengine;**  
**※5、修复打包问题，不会出现“dpkg:警告:卸载spark-uengine-runner时，目录/opt/apps/uengine-runner非空，因而不会删除该目录”的错误;**  
![1.3.2](https://storage.deepin.org/thread/202108152141139401_截图_选择区域_20210815213948.png)  

#### V1.3.1（2021-08-12）：
**※1、修复打包问题，防止部分用户安装出错的问题;**  
**※2、修复了程序无法提取图标时可以提取默认图标使用;**  
![1.3.1](https://storage.deepin.org/thread/202108121509217807_截图_选择区域_20210812150849.png)

#### V1.3.0（2021-08-08）：  
**※1、修改了界面布局;**  
**※2、修复大多数新安装普通用户的路图标及启动菜单文件路径不存在导致安装APK报错的bugs;**  
3、删除少量冗余代码，调整代码顺序;   
4、支持提取 apk 图标。   
![1.3.0](https://storage.deepin.org/thread/202108082100582804_截图_tk_20210808210047.png)

#### V1.2.3（2021-08-02）：  
1、调整部分控件名称；  
2、调整界面布局及界面风格；  
![1.2.3](https://images.gitee.com/uploads/images/2021/0802/080620_1dd289ca_7896131.png)

#### V1.2.2（2021-07-11）：  
1、对程序错误的显示更加人性化；  
2、对 icon 的获取方式进行了升级；  
3、增加了注释、删除部分冗余代码。  
![1.2.2](https://images.gitee.com/uploads/images/2021/0711/145140_b04e51b7_7896131.png)

#### V1.2.1（2021-07-02）：  
**※1、进行了安装方式的修改（不使用 adb），修复原无法安装和卸载的问题；**  
2、进行了部分优化；  
3、进行了功能缩水；  
4、修复 deb 打包错误。  
![1.2.1](https://images.gitee.com/uploads/images/2021/0702/204040_6abb6f3f_7896131.png)

#### V1.2.0（2021-06-06）：  
1、支持安装自动添加快捷方式、卸载删除快捷方式；  
2、支持使用包名或 APK 文件卸载程序；  
3、支持查看安装的所有包名；  
4、进行了部分优化  
![1.2.0](https://images.gitee.com/uploads/images/2021/0606/115536_0c0ddf38_7896131.png) 

#### V1.1.0（2021-05-30）：
1、修改了因编写时出现的中、英文混用的情况
2、支持一键连接默认 IP
3、修复在不连接设备直接选择 apk 安装时会卡住的问题
4、修复在把“uengine 程序菜单”发送到桌面或启动器如果询问覆盖时点击取消会卡住的问题
5、修改了程序界面为白色调，不和标题栏冲突矛盾
![1.1.0](https://images.gitee.com/uploads/images/2021/0530/133429_7e6bf629_7896131.png)

#### V1.0.0（2021-05-29）：
![1.0.0](https://images.gitee.com/uploads/images/2021/0529/173756_2e333c86_7896131.png)

### 源码安装教程
按下 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> 打开终端，按以下内容操作：
1.  安装所需依赖

```bash
sudo apt install python3 python3-tk git python3-pip aapt uengine
python3 -m pip install ttkthemes
```

2.  下载本程序

```bash
git clone https://gitee.com/gfdgd-xi/uengine-runner.git
```

3.  运行本程序

```bash
sudo mkdir /opt/apps/uengine-runner
sudo cp uengine-runner /opt/apps/uengine-runner -rv
sudo cp getxmlimg.py /opt/apps/uengine-runner -rv
sudo cp icon.png /opt/apps/uengine-runner -rv
chmod 777 /opt/apps/uengine-runner/main.py
sudo cp /opt/apps/uengine-runner/main.py /usr/bin/uengine-runner
./main.py
```

4.  卸载本程序
```bash
sudo rm /usr/bin/uengine-runner -v
sudo rm /opt/apps/uengine-runner/ -rfv
pip3 uninstall ttkthemes
```

### 使用说明
1、需要你有使用 root 权限的能力；  
2、需要安装 UEngine 才能使用，UOS建议在商店安装一个安卓应用，让系统自动安装 UEngine 及相关的依赖包；  
3、提取 apk 图标的 apk 路径以“安装 apk”那栏为准;  
4、如果报错是有关产生 .deksotp 文件有关，一般可以打开程序列表运行。如果想要连接其他手机，请使用 1.2.0 以前的版本，可以使用 adb 连接。  

### 故障排除
提 issue 最好，当然有些问题自己无法解决，请大佬 push 一下
如果出现故障，尝试终端运行，如果是可以自行解决的问题，就**自行解决**，如果可以就**提 issues 并提供解决方案**，不行就**提 isscue 并提供程序和终端报错以及程序版本**

### 下载量
这里只统计蓝奏云的下载量，链接（每周更新一次）：  
[https://kdocs.cn/l/smrvazWGuKcY](https://kdocs.cn/l/smrvazWGuKcY)  

### 已知问题
<p align="center"><img src='https://bbs.deepin.org/assets/image/raccoon/[sad].gif'></p>  

![Error](https://storage.deepin.org/thread/202108101105396531_截图___tk__messagebox_20210810110449.png)
部分 app 无法读取出图片，已知：
| 程序 | 下载链接 |
| :-: | :-: |
| Firefox For Android | https://www.firefox.com.cn/download/ |
| 网易云音乐 For Android | https://music.163.com/#/download |
| 抖音 | https://www.wandoujia.com/apps/7461948 |
| 360 手机浏览器 | https://mse.360.cn/ |
| E-Go | 忘了 |
| 其他待测试…… | 其他待测试…… |
**注意：提取不出图标不代表未安装成功！**


### 贡献
<p align="center"><img src='https://bbs.deepin.org/assets/image/raccoon/blush.gif'></p> 

非常欢迎大家的贡献  
贡献的开发者列表：  
| 开发者 | 邮箱 |
| :-: | :-: |
| gfdgd xi | 3025613752@qq.com |
| actionchen | 917981399@qq.com |

### 相关项目  
| 项目名称 | 项目地址 |
|   :-:  |      :-:|
| uengine-installer | https://gitee.com/Maicss/uengine-installer |  
| uengine APK 打包器 | https://gitee.com/gfdgd-xi/uengine-apk-builder |

### 附测试生成图标无问题列表：
**至于能不能用就不测试了，这暂时不是重点**
| 程序 | 下载链接 |
|:-:|:-:|
| QQ 全家桶（完整版、极速版、Android Pad 版） | https://im.qq.com |
| TIM | 忘了 |
| 微信 | https://weixin.qq.com |
| 百度翻译 | 忘了 |
| 百度网盘 | https://pan.baidu.com |
| 腾讯课堂 | 忘了 |
| 抖音极速版 | 忘了 |
| 豌豆荚 | 忘了 |
| 小猿口算 | 忘了 |
| Hyperbowl | 忘了 |
| bilibili | https://d.bilibili.com/download_app.html?bsource=app_bili |
| 蓝奏云 | https://up.woozooo.com/lanzouh5.apk |
| QQ 音乐（完整版、Android Pad 版、TV 版、车载版） | https://y.qq.com/download/index.html |
| 360 手机卫士（完整版、极速版） | https://shouji.360.cn/v6/index.html |
| 360 清理大师（稳定版、尝鲜版） | http://shouji.360.cn/360cleandroid/ |
| 360 手机助手 | http://sj.360.cn/index.html |
| WPS Office For Android | https://www.wps.cn/ |
| 钉钉 for android | https://page.dingtalk.com/wow/dingtalk/act/download?spm=a3140.8196062.0.0.6f4c5c3dWBhYUM |

### ©2021-2021