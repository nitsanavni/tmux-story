@./test/example_bash_test.yml
@./test/generated_example_bash_test.sh
@./src/dsl2bash.py

please change dsl2bash.py

B the string 2**10 (this is just an example) from the yml is evaluated by the shell in the bash script
instead, I think we should use single quotes to avoid expression expansion
