#!/bin/sh

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

picom &
nm-applet &
/home/ivopr/Applications/OneDriveGUI-1.0.3_fix150-x86_64_829883def23935cf5ac79d8db1189ef3.AppImage &

# set display timeout, sleep, and poweroff
xset s off
xset s noblank
xset -dpms

# set keyboard repeat rate
xset r rate 350 60
    