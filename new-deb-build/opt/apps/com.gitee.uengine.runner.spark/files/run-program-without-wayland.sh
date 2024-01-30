#!/bin/bash
export XDG_SESSION_TYPE=x11
export QT_QPA_PLATFORM=xcb
unset WAYLAND_DISPLAYCOPY
XDG_CURRENT_DESKTOP="Deepin"
export LD_LIBRARY_PATH=/usr/share/uengine/lib64/
"$@"
