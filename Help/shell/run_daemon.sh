#/bin/bash
# 狗头
echo '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
echo '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@`***,@@@@@@@@'
echo '@@@@^*****,\@@@@@@@@@@@@@@@@@@@@`*.....*\@@@@@@'
echo '@@@@*.......**\@[`***......*****.....*..*\@@@@@'
echo '@@@@^*..............................***...@@@@@'
echo '@@@@@*...............................**..*\@@@@'
echo '@@@@@^*..*............................*..*=@@@@'
echo '@@@@@^**................................**=@@@@'
echo '@@@@@/*..................................*=@@@@'
echo '@@@@@*.....      .....        ............*@@@@'
echo '@@@@`*. .]]]]`    ...   ]/[[[O/O]`........*,@@@'
echo '@@@@*.=`  =O.,OO......=`   .OOOOOO^........*@@@'
echo '@@@^*.\   =OOOOO^.....=`   .OOOOOO^........*=@@'
echo '@@@^*..,\].=OO/.........,[\]]O/[`    ......*=@@'
echo '@@@@*......................               .*@@@'
echo '@@@@`.    ......,]]......                 .,@@@'
echo '@@@@@*.       OOOOOOO^                   .*@@@@'
echo '@@@@@\*.       \OOOO`                   .*/@@@@'
echo '@@@@@@\*.        =.       /            .*/@@@@@'
echo '@@@@@@@@`*. ,\OOOOOOO]]OO`           .*,@@@@@@@'
echo '@@@@@@@@@@`*.               .      .*,@@@@@@@@@'
echo '@@@@@@@@@@@@\**.. .........    ..**/@@@@@@@@@@@'
echo '@@@@@@@@@@@@@@@@]`***......***,]@@@@@@@@@@@@@@@'
echo '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

# 使 UEngine 能在 Wayland 下运行
export XDG_SESSION_TYPE=x11
export QT_QPA_PLATFORM=xcb
unset WAYLAND_DISPLAYCOPY
# 判断是否是开机后第一次运行（无用）
#if [[ ! -f /tmp/uengine-loading-ubuntu ]]; then
#    # 需等待一段时间等系统全部加载完成
#    notify-send -i /opt/apps/com.gitee.uengine.runner.spark/files/icon.png "UEngine 服务正在加载" -a uengine-runner
#    sleep 10
#    touch /tmp/uengine-loading-ubuntu
#fi
# 修复程序显示问题
XDG_CURRENT_DESKTOP="Deepin"
export LD_LIBRARY_PATH=/usr/share/uengine/lib64/ 
# 判断 UEngine 是否被正确安装
which uengine
if [[ $? != 0 ]]; then
    notify-send -i /opt/apps/com.gitee.uengine.runner.spark/files/icon.png "未安装 UEngine，结束！" -a uengine-runner
    exit
fi
notify-send -i /opt/apps/com.gitee.uengine.runner.spark/files/icon.png "UEngine 服务启动完成" -a uengine-runner
bad=0
# 守护进程，防止异常退出
while [[ true ]]; do
    uengine session-manager -platformtheme=deepin
    # 让用户可以强制结束
    if [[ -f "/tmp/uengine-loading-ubuntu-end" ]]; then
        rm /tmp/uengine-loading-ubuntu-end
        echo UEngine 服务异常崩溃，不再重启服务
        notify-send -i /opt/apps/com.gitee.uengine.runner.spark/files/icon.png "UEngine 服务异常崩溃，不再重启服务" -a uengine-runner
        exit
    fi
    if [[ $bad -gt 9 ]]; then
        # 错误次数太多，结束
        notify-send -i /opt/apps/com.gitee.uengine.runner.spark/files/icon.png "UEngine 服务异常崩溃次数过多，不再重启服务" -a uengine-runner
        echo UEngine 服务异常崩溃次数过多，不再重启服务
        exit
    fi
    bad=$(($bad+1))
    echo "UEngine 服务异常结束，重新启动（$bad次）"
    notify-send -i /opt/apps/com.gitee.uengine.runner.spark/files/icon.png "UEngine 服务异常结束，重新启动（$bad次）" -a uengine-runner
    
done