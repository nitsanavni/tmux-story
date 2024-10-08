@./test/timeout.yml
@./test/generated_timeout.sh
@./src/dsl2bash.py

only change this file: dsl2bash.py

do this:
add support for timeout in the case of wait-for-output
default to 1 second
