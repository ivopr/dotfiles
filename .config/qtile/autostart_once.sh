#!/bin/bash

# Start picom
picom --config ~/.config/picom/picom.conf &

# Start polkit
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Start Network Manager Applet
nm-applet &

# set display timeout, sleep, and poweroff
xset s off
xset s noblank
xset -dpms

# set keyboard repeat rate
xset r rate 350 60
xrandr --output eDP-1 --panning 1600x900 --scale 1.171x1.171
