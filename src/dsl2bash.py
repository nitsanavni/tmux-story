import yaml
import sys
import argparse
import subprocess


def generate_bash_script(dsl, output):
    session_name = dsl['name'].lower().replace(' ', '_')
    script_lines = [
        "#!/bin/bash",
        "",
        f"# Start a tmux session in detached mode to run {dsl['base_cmd']}",
        f"tmux new-session -d -s {session_name} \"{dsl['base_cmd']}\"",
        "",
        "# Wait briefly to ensure the session starts",
        "sleep 1",
        "",
        "# Initialize a flag to track if any comparison fails",
        "any_failure=0",
        ""
    ]

    for step in dsl['story']:
        if 'send' in step:
            # Send command in the tmux session, ensuring no expression expansion
            command = step['send']
            script_lines.append(f"# Send the command: {step['send']}")
            script_lines.append(
                f"tmux send-keys -t {session_name} '{command}' Enter")
        elif 'send-no-enter' in step:
            command = step['send-no-enter']
            script_lines.append(
                f"# Send the command without Enter: {step['send-no-enter']}")
            script_lines.append(
                f"tmux send-keys -t {session_name} '{command}'")
        elif 'wait-for-output' in step:
            # Add timeout support for waiting for the expected output
            timeout = step.get('timeout', 1)  # Default to 1 second
            script_lines.append(
                f"# Wait for the specific output: {step['wait-for-output']} or timeout after {timeout} second(s)")
            script_lines.append(
                f"end_time=$((SECONDS+{timeout}))")
            script_lines.append(
                f"while ! tmux capture-pane -t {session_name} -p | grep -q \"{step['wait-for-output']}\"; do")
            script_lines.append(
                "    if [ $SECONDS -ge $end_time ]; then")
            script_lines.append(
                f"        echo \"Timeout reached while waiting for {step['wait-for-output']}\"")
            script_lines.append(
                "        any_failure=1")
            script_lines.append("        break")
            script_lines.append("    fi")
            script_lines.append(
                "    sleep 0.1  # Poll every 100ms until the output is found")
            script_lines.append("done")
        elif 'capture' in step:
            frame_name = step['capture']
            received_filename = f"{session_name}.{frame_name}.received"
            script_lines.append(f"# Capture the output in {received_filename}")
            script_lines.append(
                f"tmux capture-pane -t {session_name} -p | sed '/^$/d' > {received_filename}")
        elif 'sleep' in step:
            script_lines.append(
                f"# Wait for {step['sleep']} second(s) before next action")
            script_lines.append(f"sleep {step['sleep']}")

    # Approval testing steps
    script_lines.append("")
    for step in dsl['story']:
        if 'capture' in step:
            frame_name = step['capture']
            approved_filename = f"{session_name}.{frame_name}.approved"
            received_filename = f"{session_name}.{frame_name}.received"

            script_lines.append(
                f"# Touch the approved frame file {approved_filename}")
            script_lines.append(f"touch {approved_filename}")

            script_lines.append(
                f"# Compare received and approved frames for {frame_name}")
            script_lines.append(
                f"if ! diff {received_filename} {approved_filename} > /dev/null; then")
            script_lines.append(
                f"    echo \"Frames do not match for {frame_name}.\"")
            script_lines.append(
                "    any_failure=1  # Flag that a failure occurred")
            script_lines.append("fi")

    # Kill the tmux session before exiting
    script_lines.append("")
    script_lines.append(f"# Kill the tmux session after test")
    script_lines.append(f"tmux kill-session -t {session_name}")

    script_lines.append("if [ $any_failure -ne 0 ]; then")
    script_lines.append(
        "    echo \"At least one frame did not match. Launching vimdiff for each failure.\"")
    for step in dsl['story']:
        if 'capture' in step:
            frame_name = step['capture']
            approved_filename = f"{session_name}.{frame_name}.approved"
            received_filename = f"{session_name}.{frame_name}.received"
            script_lines.append(
                f"    if ! diff {received_filename} {approved_filename} > /dev/null; then")
            script_lines.append(
                f"        vim -d {received_filename} {approved_filename}")
            script_lines.append("    fi")
    script_lines.append("    exit 1")
    script_lines.append("fi")

    script_lines.append("echo \"All frames verified successfully.\"")
    script_lines.append("exit 0")

    # Write the generated script to the output (file or stdout)
    output.write("\n".join(script_lines))
    output.write("\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a Bash script from a DSL YAML file.")
    parser.add_argument('--test', type=str,
                        help='Path to the DSL YAML file', default='-')
    parser.add_argument('--out', type=str,
                        help='Output path for the Bash script', default='-')
    args = parser.parse_args()

    if args.test == '-':
        dsl = yaml.safe_load(sys.stdin)
    else:
        with open(args.test, 'r') as file:
            dsl = yaml.safe_load(file)

    if args.out == '-':
        generate_bash_script(dsl, sys.stdout)
    else:
        with open(args.out, 'w') as script_file:
            generate_bash_script(dsl, script_file)

    if args.out != '-':
        print(f"Bash script generated at {args.out}")


if __name__ == "__main__":
    main()
