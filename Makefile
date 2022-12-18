build:
	echo "Build DEB..."
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
	cp -rv defult.svg                     new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv defult.png                     new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv runner.svg                           new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv root-uengine.sh                      new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv menu.svg                             new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv icon.png                             new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv getxmlimg.py                         new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv defult.svg                           new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv builer.svg                           new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv api                                  new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv Help                                 new-deb-build/opt/apps/com.gitee.uengine.runner.spark/files/
	cp -rv pkexec/*                             new-deb-build/usr/share/polkit-1/actions
	python3 RemovePycacheFile.py
	dpkg -b new-deb-build com.gitee.uengine.runner.spark.deb

install:
	make build	
	echo "Install..."
	sudo apt update
	sudo dpkg -i com.gitee.uengine.runner.spark.deb ; true
	sudo apt install -f

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