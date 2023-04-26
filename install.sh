#!/bin/bash

if [[ "$(id -u)" -eq 0 ]]; then
  echo "This script must not be run as root"
  exit 1
fi

is_installed() {
  pacman -Qi "$1" &>/dev/null
  return $?
}

# Update system 
sudo pacman -Syu

if ! is_installed git; then
  sudo pacman -S git --noconfirm
else
  echo "git v$(git -v | cut -d' ' -f3) is already installed in your system"
fi

# Clone and install Paru
if command -v paru &>/dev/null; then
  echo "paru $(paru -V | cut -d' ' -f2) is already installed in your system"
else
  echo "Paru is not present in your system."
  echo "Installing paru..."
  git clone https://aur.archlinux.org/paru-bin.git && cd paru-bin && makepkg -si --noconfirm && cd ..
fi

# Update and install dependencies
if command -v paru &>/dev/null; then
  paru -Syu base-devel qtile python-psutil pywal-git picom-jonaburg-fix dunst zsh starship mpd ncmpcpp playerctl brightnessctl alacritty pfetch htop flameshot thunar roficlip rofi ranger cava pulseaudio pavucontrol neovim vim git --noconfirm  --needed
  if ! is_installed lightdm && ! is_installed sddm; then
    paru -S sddm
  fi
fi

# Check and set Zsh as the default shell
[[ "$(awk -F: -v user="$USER" '$1 == user {print $NF}' /etc/passwd) " =~ "zsh " ]] || chsh -s $(which zsh)

# Install Zsh plugins
[[ "${plugins[*]} " =~ "zsh-autosuggestions" ]] || git clone https://github.com/zsh-users/zsh-autosuggestions ~/.config/zsh/zsh-autosuggestions
[[ "${plugins[*]} " =~ "zsh-syntax-highlighting " ]] || git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.config/zsh/zsh-syntax-highlighting

# Make Backup
echo "Backing up the current configs. All the backeup files will be available at ~/.cozy.bak"
mkdir ~/.cozy.bak
for folder in .config/*; do
  rel=$(echo $folder | rev | cut -d/ -f1 | rev)
  if [ -d ~/.config/$rel ]; then
    echo "Backing up ~/.config/$rel"
    cp -r ~/.config/$rel ~/.cozy.bak
    echo "Backed up ~/.config/$rel" successfully.
    echo "Removing old config for $rel"
    rm -rf ~/.config/$rel
    echo "Copying new config for $rel"
    cp -r .config/$rel ~/.config
  else
    echo "Folder ~/.config/$rel doesn't exist"
    echo "Copying new config for $rel"
    cp -r .config/$rel ~/.config
  fi
done


cp -R ./Fonts/*/ttf ~/.local/share/fonts/

# Enable and start SDDM
if is_installed sddm; then
  sudo systemctl enable sddm && sudo systemctl start sddm
fi
