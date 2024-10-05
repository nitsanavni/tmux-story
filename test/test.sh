#!/bin/bash

cd "$(dirname "$0")"

source ../env/venv/bin/activate

# Use tmux-story for generating the script
../src/tmux-story ./example_test.yml

diff ./generated_example_test.sh ./generated_example_test.sh.approved

chmod +x generated_example_test.sh

rm -f test_python_repl_print*.received*

./generated_example_test.sh
