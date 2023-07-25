# History
HISTFILE=~/.cache/zsh
HISTSIZE=10000
SAVEHIST=10000

export VOLTA_HOME="$HOME/.volta"
export PATH="$VOLTA_HOME/bin:$HOME/.local/bin:$PATH"
export ANDROID_HOME="$HOME/Android/Sdk"

# Autosuggestions: https://github.com/zsh-users/zsh-autosuggestions
source ~/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh

# Syntax highlighting: https://github.com/zsh-users/zsh-syntax-highlighting
source ~/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Case Insensitive auto-completion
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}' 'r:|=*' 'l:|=* r:|=*'
autoload -Uz compinit && compinit

# Paths
ZSH_HIGHLIGHT_STYLES[path]='fg=blue'
# Precommand modifiers
ZSH_HIGHLIGHT_STYLES[precommand]='fg=yellow'

alias wp3="sudo docker run --privileged -ti --rm --name wifipumpkin3 --net host \"wifipumpkin3\""
alias dps="docker ps --format \"table {{.Names}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}\""

# GROMACS gmx
source /usr/local/gromacs/bin/GMXRC

# Prompt
eval "$(starship init zsh)"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/ivopr/.conda/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/ivopr/.conda/etc/profile.d/conda.sh" ]; then
        . "/home/ivopr/.conda/etc/profile.d/conda.sh"
    else
        export PATH="/home/ivopr/.conda/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<