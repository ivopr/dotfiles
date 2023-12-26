#!/bin/bash
###########################################################################################
### GNOME KEYBINDINGS BACKUP/RESTORE SCRIPT                                             ###
### ./kbdbr.sh backup|restore                                                           ###
###                                                                                     ###
### I use this with the Forge GNOME Extension, so if you don't have it, feel free to    ###
### remove or modify this file                                                          ###
###########################################################################################
set -e

mkdir -p ./keybindings

if [[ $1 == 'backup' ]]; then
  cd ./keybindings
  dconf dump /org/gnome/settings-daemon/plugins/media-keys/ > media-keybindings
  dconf dump /org/gnome/desktop/wm/keybindings/ > wm-keybindings
  dconf dump /org/gnome/shell/keybindings/ > shell-keybindings
  dconf dump /org/gnome/shell/extensions/forge/keybindings/ > forge-keybindings
  dconf dump /org/gnome/mutter/keybindings/ > mutter-keybindings
  dconf dump /org/gnome/mutter/wayland/keybindings/ > mutter-wayland-keybindings
  cd ..

  echo "Keybindings Backed up!"
  exit 0
fi

if [[ $1 == 'restore' ]]; then
  cd keybindings
  dconf load /org/gnome/settings-daemon/plugins/media-keys/ < media-keybindings
  dconf load /org/gnome/desktop/wm/keybindings/ < wm-keybindings
  dconf load /org/gnome/shell/keybindings/ < shell-keybindings
  dconf load /org/gnome/shell/extensions/forge/keybindings/ < forge-keybindings
  dconf load /org/gnome/mutter/keybindings/ < mutter-keybindings
  dconf load /org/gnome/mutter/wayland/keybindings/ < mutter-wayland-keybindings
  cd ..

  echo "Keybindings Restored!"
  exit 0
fi

echo "parameter 0: [backup|restore]"