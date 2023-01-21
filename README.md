<p width=100px align="center"><img src="runner.svg"></p>  
<h1 align="center">UEngine 运行器 1.8.3</h1>  
<hr>  
<p align='center'><a href='https://gitee.com/gfdgd-xi/uengine-runner/stargazers'><img src='https://gitee.com/gfdgd-xi/uengine-runner/badge/star.svg?theme=dark' alt='star'></img></a>  
<a href='https://gitee.com/gfdgd-xi/uengine-runner/members'><img src='https://gitee.com/gfdgd-xi/uengine-runner/badge/fork.svg?theme=dark' alt='fork'></img></a>  
  
## 介绍  
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;新版本Deepin/UOS发布后，可以在应用商店安装部分官方已适配的安卓应用，对爱好者来说，不能自己安装APK软件包始终差点意思，本程序可以为Deepin/UOS上的UEngine安卓运行环境安装自定义APK软件包，并能发送安装的APK包启动菜单到桌面或系统菜单。  
![图片.png](https://storage.deepin.org/thread/202212181918041904_图片.png)    
  
（测试平台：UOS 家庭版 21.3.1，deepin 20.8,UOS 专业版 1050）  
  
## 程序相关网站
作者个人站：https://gfdgd-xi.gitee.io  
程序论坛：http://bbs.racoongx.cn  
查询 APK 运行情况：https://gfdgd-xi.gitee.io/uengine-runner-info/  
星火应用商店：https://spark-app.store/  
星火社区：https://www.deepinos.org  
Deepin 官网：https://www.deepin.org  
Deepin 论坛：https://bbs.deepin.org  

## 安装前必读  
  
+ **UEngine 安装时会自动把要安装的 apk 删除**，如果这个 apk 文件非常重要请**拷贝一个备份版并安装这个备份版或者在程序设置里面选择“备份APK包然后在安装后自动拷贝原先目录”选项**  
  ![image.png](https://storage.deepin.org/thread/202207271700517092_image.png)  
  
## 如何升级至最新版本  
  
### 一、使用星火应用商店更新到最新版本  
  
**1、打开星火应用商店并打开到对应的界面，点击“升级”**  
![image.png](https://storage.deepin.org/thread/202205220755222083_image.png)  
**2、然后安装**  
![image.png](https://storage.deepin.org/thread/202205220756248090_image.png)  
**3、结束**  
  
### 二、通过源更新（需要添加星火应用商店源）  
  
输入以下命令即可：  
  
```bash  
sudo apt update  
sudo apt upgrade  
```  
  
![image.png](https://storage.deepin.org/thread/202205220758088497_image.png)  
  
### 三、使用程序自带的更新程序更新  
  
**1、打开 UEngine 运行器然后点击“关于”=>“检查更新”，点击“更新（更新过程中会关闭所有Python应用，包括这个应用）”**    
![image.png](https://storage.deepin.org/thread/202205220759382269_image.png)    
**2、输入密码进行更新**    
![image.png](https://storage.deepin.org/thread/202205220801175784_image.png)    
**3、提示更新完毕即可**  
![image.png](https://storage.deepin.org/thread/202205220801513371_image.png)  
  
### 更新内容  
#### V2.0.0（2023年01月22日，新春版）  
**※1、内置微型应用商店，支持评论、评分功能；**    
**※2、修复 UEngine 安装器在 Wayland 下无法正常运行的问题；**    
**※3、更新 UEngine 安装器安装的 UEngine 版本；**    
**※4、修复 UEngine 安装器安装后的 UEngine 无法正常安装 APK 的问题（包括从运行器和 deb 包安装）；**    
**※5、UEngine 安装器支持安装使用 SuperSU Root 的镜像；**    
**※6、UEngine 安装器安装后的 UEngine 支持开机后自动加载运行环境，无需人手动打开终端运行；**    
**※7、放开原先程序内的程序安装量查询功能，并新增打开量查询功能（在程序的关于窗口里打开）；**    
**※8、程序更新时不需要关闭所有 Python3 程序，只会关闭自己；**    
**※9、新增彩蛋（只在2023年1月22日生效）；**    
**※10、修复 UEngine 打包器在部分系统无法打开的问题；**    
**※11、新增程序公告功能；**    
**※12、修复了程序更新功能从高版本降级到低版本的问题；**    
**※13、不强制依赖 Deepin 终端；**    
**※14、新增 UEngine 打包器（高级版）；**    
15、更改程序论坛网址；    
16、新增程序评分功能；    
17、修复 UEngine 打包器在打包时无法正确禁用所有选项；    
18、UEngine 打包器打包的 deb 不再指定 `deepin-elf-verify` 依赖版本；    
19、“更多帮助”功能支持访问云端的帮助内容；    
20、更换程序接口；    
21、优化菜单栏分类，菜单栏新增图标；    
22、程序关于可以查看程序使用的开源协议。    
![图片.png](https://storage.deepin.org/thread/202301211303181171_图片.png)  
  
#### V1.8.3（2022年12月18日）  
**※1、修复安装/打包程序时出现找不到图标的问题；**    
**※2、修复部分无法正确获取程序中文名和 Activity 的问题；**    
**※3、修复在运行器内打开打包器不会自动填充打包器 APK 路径；**    
**※4、问题反馈新增论坛反馈入口。**    
![图片.png](https://storage.deepin.org/thread/202212181918041904_图片.png)  
  
#### V1.8.2（2022年11月28日）  
  
**※1、重新恢复 uengine-installer For Ubuntu**  
**※2、修复 postrm 的问题**  
**※3、修复“添加UEngine应用快捷方式出现问题”的问题**  
**※4、修复打包器无参数问题**  
**※5、打包器默认勾选“使用 uengine-dc 前缀”**  
6、修复Python主版本号判断时潜在的问题（By Bail）  
7、新增部分资源入口  
![image.png](https://storage.deepin.org/thread/202211282224306611_image.png)  
  
#### V1.8.1-1（2022年09月03日）  
  
**※1、修复缺失依赖 python3-matplotlib 导致程序无法开启的问题**    
**※2、移除在 Ubuntu 上用于安装 UEngine 的安装工具**    
**※3、解决了未输入密码自动回车的 bug**    
  
#### V1.8.1（2022年08月30日）  
  
**※1、修复在 APK 详细信息中图标可能过大导致无法正常使用的问题**    
**※2、修复 APK 路径带空格无法正常安装的问题**    
3、修复打包器打包的 APK 带下划线“_”无法正常打包的问题    
4、修复打包器下方命令返回过多空白行的问题    
5、修复程序生成的默认图标任然是旧版图标的问题    
![image.png](https://storage.deepin.org/thread/202208302154473781_image.png)  
  
#### V1.8.0（2022年07月27日）  
  
**※1、程序界面大部分由 Tkinter 转 PyQt5**    
**※2、添加了自动/手动配置 UEngine 窗口大小文件（自动需要在设置里手动开启，配置窗口的配置文件需要 Root）**  
**※3、增加了安装/卸载失败后的提示**  
**※4、补回谢明名单**  
**※5、支持免密安装/卸载 APK**  
6、pip 更换华为源，提升下载速度  
7、新增主题功能  
8、支持在安装 APK 后手动指定分类（手动指定需要在设置里手动开启）  
![image.png](https://storage.deepin.org/thread/202207271700065629_image.png)  
  
#### V1.7.0（2022年07月08日，暑假开始）  
  
**※1、新增暗黑主题**  
**※2、优化 deepin-terminal 在其它发行版显示奇奇怪怪的问题**  
**※3、修复 UEngine 安装脚本在安装时不让用户选择，直接默认 N 无法安装的问题**  
4、新增设置 UEngine 代理的功能  
5、将执行命令和打包器的返回输出从命令结束后显示输出内容改为实时显示内容  
![image.png](https://storage.deepin.org/thread/202207081157256904_image.png)  
  
#### V1.6.2（2022年06月21日，中考假期+即将期末考试）  
  
**※1、优化了 UEngine 运行器的英语翻译**  
**※2、新增加了可以打开或关闭第三方应用安装的功能（使用此功能后在UEngine里可以使用默认的APK安装程序安装应用，此操作需要使用程序的Adb补丁）**  
**※3、新增加了 UEngine 的 Ubuntu 安装程序**  
**※4、双包合一，只保留了UOS打包标准，可以从旧标准无缝升级（推荐使用本程序的升级程序进行升级）**  
5、修复了本程序在 Ubuntu 上安装和卸载报错而无法继续的问题  
6、优化帮助/关于窗口在高分辨率电脑上显示不全的问题  
![image.png](https://storage.deepin.org/thread/202206211816301171_image.png)  
  
#### V1.6.1（2022年05月21日，521）  
  
**※1、修复了打包 deb 包在 APK 的包名有大写时无法启动的问题**  
**※2、提供新版本的 UEngine Root 镜像**  
**※3、更新了 UEngine Root 的下载地址**  
**※4、修复了本程序的“UEngine 键盘映射”无法启动的问题**  
5、把构建 UEngine Root 镜像修改为多线程下载（wget=>aria2）  
6、提供了 UEngine 运行器的 API（可以从项目地址中获取）  
7、补上遗漏的项目参与者“星空露光”，新加参与者  
![截图_选择区域_20220521175308.png](https://storage.deepin.org/thread/202205211806261045_截图_选择区域_20220521175308.png)  
![截图_选择区域_20220521175238.png](https://storage.deepin.org/thread/202205211806269003_截图_选择区域_20220521175238.png)  
![截图_选择区域_20220521175156.png](https://storage.deepin.org/thread/202205211806255140_截图_选择区域_20220521175156.png)  
![截图_tk_20220521175128.png](https://storage.deepin.org/thread/202205211806252353_截图_tk_20220521175128.png)  
![截图_选择区域_20220521175342.png](https://storage.deepin.org/thread/202205211806254882_截图_选择区域_20220521175342.png)  
  
#### V1.6.0（开学版，开学前一天完成）  
  
**※1、更换了新的图标已完成（感谢[@星空露光](https://gitee.com/Cynorkyle)）**  
**※2、支持程序的评分和查看分数详情的功能**  
**※3、修复了在安装奇奇怪怪的安装包（如格式、标识不正确的）时的快捷方式图标为空以及快捷方式文本的变化**  
**※4、添加更新功能，可以自行升级到最新版本**  
**※5、新增程序帮助**  
6、新填彩蛋（在“关于”=>“关于”显示的窗口双击“关于”开启）  
7、修复了“UEngine 打包器”前缀选项勾选设置不生效的问题  
8、修复了“UEngine 打包器” 打包的安装包版本号带 V 无法打包的情况  
![1.6.0](https://storage.deepin.org/thread/202202122214208076_截图_选择区域_20220212221349.png)  
  
#### V1.5.3（2021-12-12，DDUC11版）：  
  
##### 更新内容  
  
**※1、修复了在 UOS 家庭版安装 apk 文件安装包信息为 None 的问题**  
**※2、“添加/删除 UEngine 图标”窗口的写入按钮在目录** `~/.local/share/icons/hicolor/256x256/apps`**不存在时点击无反应，参考报错1.5.3-1**  
**※3、修复了“UEngine APK 应用打包器”打包的deb包的.desktop文件的** `Icon`**和** `Exec`**字段有误的问题以及使用“使用前缀‘uengine-dc’”前缀的问题**  
4、“UEngine APK 应用打包器”支持打包完后自动删除临时目录  
5、“UEngine APK 应用打包器”以及“添加/删除 UEngine 图标”支持在运行出现错误时显示报错  
  
##### 报错：  
  
*1.5.3-1*  
  
```bash  
Exception in Tkinter callback  
Traceback (most recent call last):  
  File "/usr/lib/python3.7/tkinter/__init__.py", line 1705, in __call__  
    return self.func(*args)  
  File "/home/gfdgd_xi/Desktop/uengine-runner/main.py", line 865, in SaveDesktopLink  
    shutil.copy(programPath + "/defult.png", iconSavePath)  
  File "/usr/lib/python3.7/shutil.py", line 245, in copy  
    copyfile(src, dst, follow_symlinks=follow_symlinks)  
  File "/usr/lib/python3.7/shutil.py", line 121, in copyfile  
    with open(dst, 'wb') as fdst:  
FileNotFoundError: [Errno 2] No such file or directory: '/home/gfdgd_xi/.local/share/icons/hicolor/256x256/apps/com.miHoYo.cloudgames.ys.png'  
```  
  
##### 截图  
  
![1.5.3](https://storage.deepin.org/thread/202112121231595786_截图_选择区域_20211212123106.png)  
  
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
  
按下 `<kbd>`Ctrl`</kbd>`+`<kbd>`Alt`</kbd>`+`<kbd>`T`</kbd>` 打开终端，按以下内容操作：  
  
1. 安装所需依赖  
  
```bash  
sudo apt install make  
```  
  
2. 下载本程序  
  
```bash  
git clone https://gitee.com/gfdgd-xi/uengine-runner.git  
```  
  
3. 运行本程序  
  
```bash  
cd uengine-runner  
make run  
```  
  
如果你想要安装到系统，只需要输入：  
  
```bash  
make install  
```  
  
即可  
  
### 使用说明  
  
1、需要你有使用 root 权限的能力；  
2、需要安装 UEngine 才能使用，UOS建议在商店安装一个安卓应用，让系统自动安装 UEngine 及相关的依赖包；  
3、提取 apk 图标的 apk 路径以“安装 apk”那栏为准;  
4、如果报错是有关产生 .deksotp 文件有关，一般可以打开程序列表运行。如果想要连接其他手机，请使用 1.2.0 以前的版本，可以使用 adb 连接。  
  
### 故障排除  
  
提 issue 最好，当然有些问题自己无法解决，请大佬 push 一下  
如果出现故障，尝试终端运行，如果是可以自行解决的问题，就**自行解决**，如果可以就**提 issues 并提供解决方案**，不行就**提 isscue 并提供程序和终端报错以及程序版本**  
  
### 已知问题  
  
<p align="center"><img src='https://bbs.deepin.org/assets/image/raccoon/[sad].gif'></p>  
  
![Error](https://storage.deepin.org/thread/202108101105396531_截图___tk__messagebox_20210810110449.png)  
部分 app 无法读取出图片，已知：  
  
|          程序          |                下载链接                |  
| :--------------------: | :------------------------------------: |  
|  Firefox For Android  |  https://www.firefox.com.cn/download/  |  
| 网易云音乐 For Android |    https://music.163.com/#/download    |  
|          抖音          | https://www.wandoujia.com/apps/7461948 |  
|     360 手机浏览器     |          https://mse.360.cn/          |  
|          E-Go          |        http://www.xiaojump.com/        |  
|     其他待测试……     |             其他待测试……             |  
  
**注意：提取不出图标不代表未安装成功！**  
  
### 贡献  
  
<p align="center"><img src='https://bbs.deepin.org/assets/image/raccoon/blush.gif'></p>  
  
非常欢迎大家的贡献  
贡献的开发者列表：    
  
|            开发者            |              邮箱              |  
| :--------------------------: | :----------------------------: |  
|           gfdgd xi           |       3025613752@qq.com       |  
|          actionchen          |        917981399@qq.com        |  
|             柚子             |    https://gitee.com/Limexb    |  
|           星空露光           |  https://gitee.com/Cynorkyle  |  
| 为什么您不喜欢熊出没和阿布呢 | https://weibo.com/u/7755040136 |  
  
### 相关项目  
  
|      项目名称      |                    项目地址                    |  
| :----------------: | :--------------------------------------------: |  
| uengine-installer |   https://gitee.com/Maicss/uengine-installer   |  
| UEngine APK 打包器 | https://gitee.com/gfdgd-xi/uengine-apk-builder |  
|    Root UEngine    |     https://gitee.com/Limexb/root-uengine     |  
  
### UEngine 运行器的部分技术介绍  
  
可见：https://www.52pojie.cn/thread-1672077-1-1.html  
  
### 附测试生成图标无问题列表：  
  
**至于能不能用就不测试了，这暂时不是重点**  
**现在新加了评分功能，就看大家的评分了！**    
  
|                                                              程序                                                              |                                         下载链接                                         |  
| :-----------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------: |  
|                                           QQ 全家桶（完整版、极速版、Android Pad 版）                                           |                                    https://im.qq.com                                    |  
|                                                               TIM                                                               |                           https://office.qq.com/download.html                           |  
|                                                              微信                                                              |                                  https://weixin.qq.com                                  |  
|                                                            百度翻译                                                            |                    https://fanyi.baidu.com/appdownload/download.html                    |  
|                                                            百度网盘                                                            |                                  https://pan.baidu.com                                  |  
|                                                            腾讯课堂                                                            |                           https://ke.qq.com/download/app.html                           |  
|                                                           抖音极速版                                                           |                         https://www.douyin.com/downloadpage/app                         |  
|                                                             豌豆荚                                                             |                                https://www.wandoujia.com/                                |  
|                                                            小猿口算                                                            |                              http://kousuan.yuanfudao.com/                              |  
|                                                            Hyperbowl                                                            |                                         忘了/无                                         |  
|                                                            bilibili                                                            |                https://d.bilibili.com/download_app.html?bsource=app_bili                |  
|                                                             蓝奏云                                                             |                           https://up.woozooo.com/lanzouh5.apk                           |  
|                                        QQ 音乐（完整版、Android Pad 版、TV 版、车载版）                                        |                           https://y.qq.com/download/index.html                           |  
|                                                 360 手机卫士（完整版、极速版）                                                 |                           https://shouji.360.cn/v6/index.html                           |  
|                                                 360 清理大师（稳定版、尝鲜版）                                                 |                           http://shouji.360.cn/360cleandroid/                           |  
|                                                          360 手机助手                                                          |                               http://sj.360.cn/index.html                               |  
|                                                     WPS Office For Android                                                     |                                   https://www.wps.cn/                                   |  
|                                                        钉钉 for android                                                        | https://page.dingtalk.com/wow/dingtalk/act/download?spm=a3140.8196062.0.0.6f4c5c3dWBhYUM |  
  
### ©2021-Now  
