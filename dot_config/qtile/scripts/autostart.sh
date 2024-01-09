#!/bin/bash

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

nm-applet &

# set display timeout, sleep, and poweroff
xset s off
xset s noblank
xset -dpms

# set keyboard repeat rate
xset r rate 350 60
