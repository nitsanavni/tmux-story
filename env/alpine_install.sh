#!/bin/sh
set -euo pipefail

which tmux
if [ $? -eq 0 ]; then
    echo "tmux is already installed"
else
    apk add tmux
fi
tmux -V


which python3
if [ $? -eq 0 ]; then
    echo "python3 is already installed"
else
    apk add python3
fi

python3 --version

which pip3

if [ $? -eq 0 ]; then
    echo "pip3 is already installed"
else
    apk add py3-pip
fi

pip3 --version

which bash

if [ $? -eq 0 ]; then
    echo "bash is already installed"
else
    apk add bash
fi

which vim

if [ $? -eq 0 ]; then
    echo "vim is already installed"
else
    apk add vim
fi

