import yaml

def generate_bash_script(dsl_path: str, output_path: str):
    with open(dsl_path, 'r') as file:
        dsl = yaml.safe_load(file)

    script_lines = [
        "#!/bin/bash",
        "",
        f"# Start a tmux session in detached mode to run {dsl['base_cmd']}",
        f"tmux new-session -d -s {dsl['name'].lower().replace(' ', '_')} \"{dsl['base_cmd']}\"",
        "",
        "# Wait briefly to ensure the session starts",
        "sleep 1",
        ""
    ]

    for step in dsl['story']:
        if 'send' in step:
            # Send command in the tmux session
            script_lines.append(f"# Send the command: {step['send']}")
            script_lines.append(f"tmux send-keys -t {dsl['name'].lower().replace(' ', '_')} \"{step['send']}\" Enter")
        elif 'wait-for-output' in step:
            # Wait until the expected output appears
            script_lines.append(f"# Wait for the specific output: {step['wait-for-output']}")
            script_lines.append(f"while ! tmux capture-pane -t {dsl['name'].lower().replace(' ', '_')} -p | grep -q \"{step['wait-for-output']}\"; do")
            script_lines.append("    sleep 0.1  # Poll every 100ms until the output is found")
            script_lines.append("done")
        elif 'capture' in step:
            # Capture the output to a file
            script_lines.append(f"# Capture the output in {step['capture']}.txt")
            script_lines.append(f"tmux capture-pane -t {dsl['name'].lower().replace(' ', '_')} -p > {step['capture']}.txt")
        elif 'sleep' in step:
            # Sleep for the specified number of seconds
            script_lines.append(f"# Wait for {step['sleep']} second(s) before next action")
            script_lines.append(f"sleep {step['sleep']}")
    
    # Kill the tmux session
    script_lines.append("")
    script_lines.append(f"# Kill the tmux session after test")
    script_lines.append(f"tmux kill-session -t {dsl['name'].lower().replace(' ', '_')}")

    # Write the generated script to the output file
    with open(output_path, 'w') as script_file:
        script_file.write("\n".join(script_lines))

    print(f"Bash script generated at {output_path}")


# Example usage
dsl_path = 'dsl_example.yml'
output_path = 'generated_test_script.sh'
generate_bash_script(dsl_path, output_path)
