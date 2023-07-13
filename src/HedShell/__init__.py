from .core import (
    shell_input, 
    execute_command,
    EMPTY_COMMAND, 
    print_documentation,
    load_commands
)

from sys import argv 

def run() -> None:
    """ Code that runs the shell. """
    
    if len(argv) > 1:
        load_commands(argv[1:])
        return

    print_documentation()
    while True: 
        command = shell_input()

        if command != EMPTY_COMMAND: 
            execute_command(command)
