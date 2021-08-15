# uengine 运行器 1.3.2

### 介绍
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;新版本Deepin/UOS发布后，可以在应用商店安装部分官方已适配的安卓应用，对爱好者来说，不能自己安装APK软件包始终差点意思，本程序可以为Deepin/UOS上的Uengine安卓运行环境安装自定义APK软件包，并能发送安装的APK包启动菜单到桌面或系统菜单。  
![主界面](https://storage.deepin.org/thread/202108152141139401_截图_选择区域_20210815213948.png)  
（测试平台：UOS 家庭版，deepin 20.2.2,UOS 专业版 1040）   
（自己美术功底太差，图标直接用 anbox 的了）   

### 更新内容

#### V1.3.2：
**※1、支持uengine数据重置;**
**※2、支持修改uengine网络桥接的启动状态;**
**※3、支持右键安装/卸载;**
**※4、支持启用或禁用uengine;**
**※5、修复打包问题，不会出现“dpkg:警告:卸载spark-uengine-runner时，目录/opt/apps/uengine-runner非空，因而不会删除该目录”的错误;**
![1.3.2](https://storage.deepin.org/thread/202108152141139401_截图_选择区域_20210815213948.png)  

#### V1.3.1：
**※1、修复打包问题，防止部分用户安装出错的问题;**
**※2、修复了程序无法提取图标时可以提取默认图标使用;**
![1.3.1](https://storage.deepin.org/thread/202108121509217807_截图_选择区域_20210812150849.png)

#### V1.3.0：  
**※1、修改了界面布局;**  
**※2、修复大多数新安装普通用户的路图标及启动菜单文件路径不存在导致安装APK报错的bugs;**  
3、删除少量冗余代码，调整代码顺序;   
4、支持提取 apk 图标。   
![1.3.0](https://storage.deepin.org/thread/202108082100582804_截图_tk_20210808210047.png)

#### V1.2.3：  
1、调整部分控件名称；  
2、调整界面布局及界面风格；  
![1.2.3](https://images.gitee.com/uploads/images/2021/0802/080620_1dd289ca_7896131.png)

#### V1.2.2：  
1、对程序错误的显示更加人性化；  
2、对 icon 的获取方式进行了升级；  
3、增加了注释、删除部分冗余代码。  
![1.2.2](https://images.gitee.com/uploads/images/2021/0711/145140_b04e51b7_7896131.png)

#### V1.2.1：  
**※1、进行了安装方式的修改（不使用 adb），修复原无法安装和卸载的问题；**  
2、进行了部分优化；  
3、进行了功能缩水；  
4、修复 deb 打包错误。  
![1.2.1](https://images.gitee.com/uploads/images/2021/0702/204040_6abb6f3f_7896131.png)

#### V1.2.0：  
1、支持安装自动添加快捷方式、卸载删除快捷方式；  
2、支持使用包名或 APK 文件卸载程序；  
3、支持查看安装的所有包名；  
4、进行了部分优化  
![1.2.0](https://images.gitee.com/uploads/images/2021/0606/115536_0c0ddf38_7896131.png) 

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
2、需要安装 uengine 才能使用，UOS建议在商店安装一个安卓应用，让系统自动安装uengine及相关的依赖包；  
3、提取 apk 图标的 apk 路径以“安装 apk”那栏为准;  
4、如果报错是有关产生 .deksotp 文件有关，一般可以打开程序列表运行。如果想要连接其他手机，请使用 1.2.0 以前的版本，可以使用 adb 连接。  

### 故障排除
提 issue 最好，当然有些问题自己无法解决，请大佬 push 一下
如果出现故障，尝试终端运行，如果是可以自行解决的问题，就**自行解决**，如果可以就**提 issues 并提供解决方案**，不行就**提 isscue 并提供程序和终端报错以及程序版本**

### 已知问题
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
我非常欢迎大家的贡献  
有通过贡献的开发者列表：  
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