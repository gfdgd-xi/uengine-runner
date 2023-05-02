clean:
	python3 RemovePycacheFile.py

build:
	echo 别云间
	echo 三年羁旅客，今日又南冠。
	echo 无限山河泪，谁言天地宽。
	echo 已知泉路近，欲别故乡难。
	echo 毅魄归来日，灵旗空际看。 
	echo
	echo 译文：三年为抗清兵东走西飘荡，今天兵败被俘作囚入牢房。无限美好河山失陷伤痛泪，谁还敢说天庭宽阔地又广。已经知道黄泉之路相逼近，想到永别故乡实在心犯难。鬼雄魂魄等到归来那一日，灵旗下面要将故乡河山看。
	echo "Build DEB..."
	cp -rv uengine-loading-ubuntu.desktop       new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv information.json                     new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv mainwindow.py                        new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/uengine-runner
	cp -rv Language.json                        new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-window-size-setting.py       new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-keyboard                     new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-apk-builder                  new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-useadb                       new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-runner-update-bug            new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-runner-applist-launch.sh     new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv launch.sh                            new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-installer                    new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv LICENSE                              new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-runner-launch.sh             new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-runner-about                 new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-clean                        new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-app-uninstall                new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-app-setting.py               new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-app-install                  new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine_logo.svg                     new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv defult.svg                           new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv defult.png                           new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv runner.svg                           new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv root-uengine.sh                      new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv menu.svg                             new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv icon.png                             new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv getxmlimg.py                         new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv defult.svg                           new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv builer.svg                           new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-apk-builder-more             new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv api                                  new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv Help                                 new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv Download.py                          new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv updatekiller.py                      new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv pkexec/*                             new-deb-build/usr/share/polkit-1/actions
	cp -rv AutoShell                            new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv AutoConfig.py                        new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv Model                                new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv UI                                   new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv ConfigLanguareRunner-help.json       new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv ConfigLanguareRunner.py              new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv run-program-without-wayland.sh       new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv ProgramFen.py                        new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv Icon                                 new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv CompareVersion.py                    new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv uengine-remove.sh                    new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv pkexec                               new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv LoadingBinder                        new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	rm -rfv new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/Help/information
	python3 UpdateTime.py
	python3 RemovePycacheFile.py                #new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv new-deb-build /tmp/uengine-runner-builder
	sudo chown -R root:root /tmp/uengine-runner-builder
	sudo dpkg -b /tmp/uengine-runner-builder com.gitee.uengine.runner.spark.deb
	sudo rm -rfv /tmp/uengine-runner-builder

install:
	make build	
	echo "Install..."
	sudo apt update
	#sudo dpkg -i com.gitee.uengine.runner.spark.deb | true
	#sudo apt install -f
	sudo apt reinstall ./com.gitee.uengine.runner.spark.deb
	sudo rm com.gitee.uengine.runner.spark.deb

depend:
	sudo apt install python3 python3-tk python3-pip aapt \
	python3-setuptools deepin-terminal curl python3-pil\
	 python3-requests adb fonts-noto-cjk python3-numpy\
	  python3-matplotlib wget inotify-tools aria2 python3-pyqt5
	python3 -m pip install --upgrade pip          --trusted-host https://repo.huaweicloud.com -i https://repo.huaweicloud.com/repository/pypi/simple
	python3 -m pip install --upgrade ttkthemes    --trusted-host https://repo.huaweicloud.com -i https://repo.huaweicloud.com/repository/pypi/simple
	python3 -m pip install --upgrade pyautogui    --trusted-host https://repo.huaweicloud.com -i https://repo.huaweicloud.com/repository/pypi/simple
	python3 -m pip install --upgrade keyboard     --trusted-host https://repo.huaweicloud.com -i https://repo.huaweicloud.com/repository/pypi/simple

run:
	python3 mainwindow.py