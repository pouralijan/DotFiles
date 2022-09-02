#!/usr/bin/env bash

DOTFILES_PATH=/home/${USER}/.dotfiles/ 

git clone --bare  https://github.com/pouralijan/DotFiles.git ${DOTFILES_PATH}
mkdir -p .config-backup && \
dotfiles checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | xargs -I{} mv {} .config-backup/{}
dotfiles checkout
dotfiles config --local status.showUntrackedFiles no
