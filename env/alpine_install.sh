#!/bin/sh -e

which tmux || apk add tmux
tmux -V

which python3 || apk add python3
python3 --version

which pip3 || apk add py3-pip
pip3 --version

which bash || apk add bash

which vim || apk add vim
