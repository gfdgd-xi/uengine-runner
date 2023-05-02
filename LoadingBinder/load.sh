#!/bin/bash
if [[ `whoami` != root ]]; then
    echo 这不是 root 用户，结束
    exit 1
modprobe binder_linux
mkdir /dev/binderfs
mount -t binder binder /dev/binderfs