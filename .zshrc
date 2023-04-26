# History
HISTFILE=~/.cache/zsh
HISTSIZE=10000
SAVEHIST=10000

export VOLTA_HOME="$HOME/.volta"
export PATH="$VOLTA_HOME/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"

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