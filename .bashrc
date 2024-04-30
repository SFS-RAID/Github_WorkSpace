# ~/.bashrc: executed by bash (1) for non-login shells.
# Note: PS1 and umask are already set in /etc/profile. You should not
# need this unless you want different defaults for root.

# PS1='${debian_chroot:+($debian_chroot)}\h:\w\$'
# PS1='\[\033[1;36m\]\w \[\033[1;31m\]>\[\033[0m\] '

# Define colors
PURPLE='\[\033[1;35m\]'
RED='\[\033[1;31m\]'
CYAN='\[\033[1;36m\]'
GREEN='\[\033[1;32m\]'
GRAY='\[\033[1;37m\]'
RESET='\[\033[0m\]'

# Customize PS1 prompt
PS1="\n${RED}[${CYAN}\u@${CYAN}\h${RED}] - [${GREEN}\w${GREEN}${RED}] - [${PURPLE} \d \@ ${RED}]\n${CYAN}\$ -> ${RESET}"

# You may uncomment the following lines if you want 'ls' to be colorized:
export LS_OPTIONS='--color=auto'
eval "$(dircolors --sh)"
alias ls='eza'
alias ll='eza -L'
alias l='eza -LA'
alias la='eza -a'

# Some more alias to avoid making mistakes:
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias vncstop='rm -rf /tmp/.*X*-*'

source commands.sh
source print.sh


export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
