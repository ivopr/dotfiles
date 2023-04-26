#!/bin/bash

# Apply wallpaper using wal
wal -i ~/Wallpaper/claudio-testa-FrlCwXwbwkk-unsplash.jpg &

# Start picom
picom --config ~/.config/picom/picom.conf &


# Start Network Manager Applet
nm-applet &

# set display timeout, sleep, and poweroff
xset s off
xset s noblank
xset -dpms

# set keyboard repeat rate
xset r rate 350 60

gummy start
gummy -t 4000