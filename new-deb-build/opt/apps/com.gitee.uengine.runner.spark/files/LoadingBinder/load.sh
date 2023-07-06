#!/bin/bash
if [[ `whoami` != root ]]; then
    echo 这不是 root 用户，结束
    exit 1
fi
if [ -d /dev/binderfs ]; then   
    echo 已启动 binder，end
    systemctl start uengine-container.service
    systemctl start uengine-session.service
    exit
fi
modprobe binder_linux
modprobe ashmem_linux
mkdir /dev/binderfs
mount -t binder binder /dev/binderfs
systemctl start uengine-container.service
systemctl start uengine-session.service
