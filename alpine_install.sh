#!/bin/sh

apk add tmux
tmux -V

# Install Python
apk add python3
python3 --version
