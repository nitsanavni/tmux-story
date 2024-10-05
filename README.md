tmux-story

A e2e approval testing utility for cli apps that uses tmux.

## Example test

```yml
name: Test Python REPL Print
base_cmd: python3 -q
story:
  - send: print("Hello, world!")
  - capture: hello
  - send: 2**10
  - wait-for-output: 1024
  - send: print("Goodbye, world!")
  - capture: goodbye
  - sleep: 1
```

The two captured frames in this story are verified, in the approval-tests way.

## Build and (self-)test

```sh
./build-and-test
```

This script supports: Alpine Linux.
