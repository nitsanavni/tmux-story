#!/bin/sh
set -euo pipefail

cd "$(dirname "$0")"

./alpine_install.sh

python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

