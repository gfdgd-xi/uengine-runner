#!/bin/bash

# 忽略社区版检测

pkgRunCnt=`ps -ef |grep "uengine launch" |grep -v grep |grep "$pkg" |wc -l`
if [ $pkgRunCnt -ge 1 ]; then
    #防止短时间内多次打开同一应用，如果应用正在启动中，此次忽略
    exit 0
fi

#等Session服务启动完全
wscont=0
isReady=`busctl --user get-property org.anbox /org/anbox org.anbox.ApplicationManager Ready`
if [ "$isReady" != "b true" ] ;then
    sleep 2
fi
while [ "$isReady" = "b false" -a $wscont -lt 10 ]
do
    sleep 1
    isReady=`busctl --user get-property org.anbox /org/anbox org.anbox.ApplicationManager Ready`
    let wscont++
done

uengine launch $*
