from .core import (
    shell_input, 
    execute_command,
    EMPTY_COMMAND, 
    print_documentation,
)

def run() -> None:
    """ Code that runs the shell. """
    print_documentation()
    while True: 
        command = shell_input()
        if command != EMPTY_COMMAND: execute_command(command)




