# API 介绍
# 必知
1. 此 API 只支持可以运行 UEngine 的 Linux 上，Windows 上无法使用
2. 部分函数需要 root 权限
3. 这是 UEngine 运行器的函数重构，所以一些 UEngine 运行器上没有的 bug 可能在这个 API 里有
## ProgramInformation
用于获取一些程序信息，详细如下（此为变量）：
| 变量名 | 变量介绍 |
|:-:|:-:|
| programPath | 获取程序所在路径 |
| version | API 版本 |
| updateTime | 更新时间 |
| websize | 程序官网 |

## Check
用于检查 API 所需的东西是否完整，详细如下：  
| 函数名 | 函数介绍 |
|:-:|:-:|
| CheckDepend() | 检查 API 所需的依赖是否完整 |  

## ROOT
用于检查 ROOT 方面问题，详细如下：
| 函数名 | 函数介绍 |
|:-:|:-:|
| GetRoot() | 检查程序/API是否以 ROOT 权限运行 |

## APK
这是面向对象的写法，所以应用方式也不一样：
```python
import api
xxx = api.APK("APK 所在路径")
```
具体函数介绍：  
| 函数名 | 函数介绍 |
|:-:|:-:|
| xxx.install() | 安装这个 APK 包 |
| xxx.uninstall()| 卸载这个 APK 包 |
| xxx.information()| 获取从 aapt 获取到的 APK 信息 |
| xxx.activityName() | 获取 APK 的 Activity 信息 |
| xxx.packageName() | 获取 APK 包名 |
| xxx.chineseLabel() | 获取 APK 中文名称 |
| xxx.saveApkIcon("图标保存路径") | 保存 APK 的图标到指定路径 |
| xxx.version() | 获取 APK 版本号 |

## UEngine
用于对 UEngine 进行一点点操控，详细如下：
| 函数名 | 函数介绍 |
|:-:|:-:|
| CPUCheck() | 检查 CPU 是否支持运行 UEngine |
| Services | 用于操控 UEngine 服务的类，见下 |
| InternetBridge | 用于操控 UEngine 网络桥接的类，见下 |
### Services
关于 UEngine 的服务控制：
| 函数名 | 函数介绍 |
|:-:|:-:|
| Services.Open() | 打开 UEngine 服务 | 
| Services.Close() | 关闭 UEngine 服务 |
| Services.Restart() | 重启 UEngine 服务 |
### InternetBridge
关于 UEngine 的网络桥接控制：
| 函数名 | 函数介绍 |
|:-:|:-:|
| InternetBridge.Open() | 打开 UEngine 网络桥接 | 
| InternetBridge.Close() | 关闭 UEngine 网络桥接 |
| InternetBridge.Restart() | 重启 UEngine 网络桥接 |
| InternetBridge.Reload() | 重新加载 UEngine 网络桥接 |
| InternetBridge.ForceReload() | 强制加载 UEngine 网络桥接 |