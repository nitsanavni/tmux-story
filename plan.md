# Ideas

- timeout: fail fast

- quotes escape issue
  - try with `send: [|>]` style
- trap session kill
- capture: default name
- capture: add field to allow capturing more than visible on pane
- yaml schema
- idea: dsl interpreter, exec each step at a time
- constraints.txt?
- if the base_cmd fails, need to capture the err
- ci: scripts do not fail on err
- OS compatibility?
  - we could at least fall back to 'human do task'; e.g. 'please install tmux'
- less dependencies: don't need `vim -d`
- aliases:
  - verify, capture, frame
  - steps, story
- outer/inner test: generation_test.sh / generated_script_test.sh
- unit tests
  - modularize
- should we unlink received files on success?

# Done

- timeout
- nicer directory structure
- [x] B the string 2**10 from the yml is evaluated by the shell in the bash script
- [x] `dev-install.sh`: setup a dev env on a clean gitpod
- [x] `build-and-test`
  - clean machine - try on alpine in gitpod
  - `install.sh`
    - `alpine_install.sh`
    - installs
      - ? diff
      - python
      - tmux
    - requirements.txt
  - `test.sh`
    - outer: generate -> verify
    - inner: exec after rm received files
