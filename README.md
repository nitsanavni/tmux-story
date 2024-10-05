tmux-story

A e2e approval testing framework for cli apps that uses tmux.

## Example test

```yml
name: "Test Python REPL Print"
base_cmd: "python3 -q"
story:
  - send: "print('Hello, world!')"
  - capture: "hello"
  - send: "2**10"
  - wait-for-output: "1024"
  - send: "print('Goodbye, world!')"
  - sleep: 1
  - capture: "goodbye"
```

The two captured frames in this story are verified, in the approval-tests way.

## Build and (self-)test

```sh
./build-and-test
```

This script supports: Alpine Linux.
