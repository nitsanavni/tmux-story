#!/bin/bash

cd "$(dirname "$0")"

source ../env/venv/bin/activate

cat ./example_test.yml | python3 ../src/dsl2bash.py > generated_example_test.sh

diff ./generated_example_test.sh ./generated_example_test.sh.approved

chmod +x generated_example_test.sh

rm -f test_python_repl_print*.received*

./generated_example_test.sh

