#!/bin/sh

apk add tmux
tmux -V

# Install Python
apk add python3 py3-pip
python3 --version

# Install Bash
apk add bash

apk add vim

