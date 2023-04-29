#!/bin/bash
sudo apt purge uengine uengine-modules-dkms uengine-android-image -y
sudo rm /usr/share/applications/uengine-loading-ubuntu.desktop
sudo rm /etc/xdg/autostart/uengine-loading-ubuntu.desktop
sudo rm /usr/bin/uengine-loading-ubuntu
for username in $(ls /home)  
do
    echo /home/$username
    sudo rm /home/$username/uengine-launch/run_daemon.sh
done