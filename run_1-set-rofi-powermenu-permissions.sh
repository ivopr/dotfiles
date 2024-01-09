#!/bin/sh

FILE="$HOME/.config/rofi/scripts/power"
if [ -f "$FILE" ]; then
    if [ "$(stat -c %a "$FILE")" != "755" ] ; then
        chmod 755 "$FILE"
    fi
fi
