#!/bin/bash

file="/data/uengine/data/data/data/com.tencent.mm/shared_prefs/"
inotifywait -mq -e modify $file | while read event
	do
		if [[ "$event" == *notify_sync_pref.xml ]];then
			notify-send -i '/home/tensor/Documents/notify/mm.jpg' ‘主银’ ‘你有微信消息哦～～’
		fi
	done

