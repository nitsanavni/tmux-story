#!/bin/sh

./alpine_install.sh

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

