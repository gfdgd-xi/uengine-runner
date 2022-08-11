#!/bin/bash
#########################################################################
# 作者：gfdgd xi、为什么您不喜欢熊出没和阿布
# 版本：1.8.1
#########################################################################
#################
# 引入所需的库
#################
echo 'mmmmm                                    '
echo '#   "# m   m  m mm   m mm    mmm    m mm '
echo '#mmmm" #   #  #"  #  #"  #  #"  #   #"  "'
echo '#   "m #   #  #   #  #   #  #""""   #    '
echo '#    " "mm"#  #   #  #   #  "#mm"   #    '
echo
echo
while [ true ]
do
    echo "请输入 APK 路径或将 APK 文件拖入此处"
    read path
    if [ ! -d $path ]; then
        echo APK路径不存在，请重新输入
        echo
        continue
    fi
    uengine install --apk='$path'
done