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
  paru -Syu base-devel qtile ttf-firacode-nerd ttf-fira-code python-psutil picom-jonaburg-fix dunst zsh starship brightnessctl alacritty htop flameshot rofi ranger cava gnome-keyring lxappearance pavucontrol github-cli google-chrome visual-studio-code-bin upower qt5-graphicaleffects alsa-utils sddm imagemagick qt5-quickcontrols2 xz qt5-svg nodejs-lts-hydrogen npm network-manager-applet --noconfirm --needed
fi

if ! command -v pnpm &>/dev/null; then
  sudo npm i -g pnpm
fi

if ! command -v yarn &>/dev/null; then
  sudo npm i -g yarn
fi

# Check and set Zsh as the default shell
[[ "$(awk -F: -v user="$USER" '$1 == user {print $NF}' /etc/passwd) " =~ "zsh " ]] || chsh -s $(which zsh)

# Install Zsh plugins
if [ ! -d "$HOME/.config/zsh/zsh-autosuggestions" ]; then
  git clone https://github.com/zsh-users/zsh-autosuggestions ~/.config/zsh/zsh-autosuggestions
fi

if [ ! -d "$HOME/.config/zsh/zsh-syntax-highlighting" ]; then
  git clone https://github.com/zsh-users/zsh-syntax-highlighting ~/.config/zsh/zsh-syntax-highlighting
fi


cp -r .icons $HOME
cp -r .themes $HOME

# Make Backup
echo "Backing up the current configs. All the backed up files will be available at ~/.config.bak"
if [ ! -d ~/.config.bak ]; then
  mkdir ~/.config.bak
fi
for folder in .config/*; do
  rel=$(echo $folder | rev | cut -d/ -f1 | rev)
  if [ ! $rel = "Code" ]; then
    echo "Backing up ~/.config/$rel"
    cp -r ~/.config/$rel ~/.config.bak
    rm -rf ~/.config/$rel
    echo "Copying new config for $rel"
    cp -r .config/$rel ~/.config
  fi
done

cp .zshrc ~/.zshrc

if [ ! -f "/etc/sddm.conf" ]; then
  sudo mkdir -p /usr/share/sddm/themes
  sudo xz -xf ./sugar-candy.tar.gz -C /usr/share/sddm/themes

  sudo cp sddm.conf /etc/sddm.conf
fi

# Enable and start SDDM
if is_installed sddm; then
  sudo systemctl enable sddm && sudo systemctl start sddm
fi
