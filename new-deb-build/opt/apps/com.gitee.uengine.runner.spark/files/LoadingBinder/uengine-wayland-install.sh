#!/bin/bash
programPath=$(cd $(dirname $0); pwd)
if [[ ! -f /usr/bin/uengine ]]; then
    echo 未安装uengine，请先安装！
    exit 1
fi
if [[ -f /usr/bin/uengine-session ]] ;then
    echo 已经安装补丁，无需重复安装！
    exit 1
fi
sudo mv /usr/bin/uengine /usr/bin/uengine-session 
sudo cp "$programPath/uengine" /usr/bin/uengine 
sudo chmod +x /usr/bin/uengine
sudo systemctl restart uengine-session.service
echo 补丁安装完成！