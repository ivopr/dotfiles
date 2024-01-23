#!/bin/sh

FILE="$HOME/.config/qtile/scripts/autostart.sh"
if [ -f "$FILE" ]; then
    if [ "$(stat -c %a "$FILE")" != "755" ] ; then
        chmod 755 "$FILE"
    fi
fi