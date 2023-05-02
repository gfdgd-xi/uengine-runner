#/bin/bash
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
notify-send -i /opt/apps/com.gitee.uengine.runner.spark/files/icon.png "UEngine 服务启动完成" -a uengine-runner
# 守护进程，防止异常退出
while [[ true ]]; do
    uengine session-manager -platformtheme=deepin
    notify-send -i /opt/apps/com.gitee.uengine.runner.spark/files/icon.png "UEngine 服务异常结束，重新启动" -a uengine-runner
done