#!/bin/bash

cd "$(dirname "$0")"

source ../env/venv/bin/activate

rm -f test_python_repl_print*.received*

../src/tmux-story ./example_test.yml

diff ./generated_example_test.sh ./generated_example_test.sh.approved
