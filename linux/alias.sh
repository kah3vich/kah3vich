# unalias -m '*' # delete all aliases

alias -- -='cd -'
alias -g ...=../..
alias -g ....=../../..
alias -g .....=../../../..
alias -g ......=../../../../..

alias c='clear'
alias rf='rm -rf'
alias rz='exec zsh'
alias conf='code ~/.zshrc'
alias ls='ls --color=auto -al'
alias s='cd ~; clear; exec zsh'
