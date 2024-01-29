#!/bin/bash
# 判断是不是 Deepin23
cat /etc/deepin_version | grep 23
if [[ $? != 0 ]]; then
	# 如果不是
	# 判断系统是否有安装 aapt
	which aapt > /dev/null
	if [[ $? == 0 ]]; then
		# 如果有安装
		aapt "$@"
		exit $?
	fi
fi
# 如果是
programPath=$(cd $(dirname $0); pwd)
echo $programPath
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$programPath"
$programPath/aapt "$@"
exit $?
