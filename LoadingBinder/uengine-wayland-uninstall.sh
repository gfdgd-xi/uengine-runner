#!/bin/bash
programPath=$(cd $(dirname $0); pwd)
if [[ ! -f /usr/bin/uengine ]]; then
    echo 未安装uengine，请先安装！
    exit 1
fi
if [[ ! -f /usr/bin/uengine-session ]] ;then
    echo 未安装补丁，无需卸载！
    exit 1
fi
rm -fv /usb/bin/uengine
sudo mv /usr/bin/uengine-session /usr/bin/uengine 
sudo chmod +x /usr/bin/uengine
sudo systemctl restart uengine-session.service
echo 补丁卸载完成！