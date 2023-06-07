
"""

Author: Hossin azmoud (Moody0101)
Date: 10/18/2022
LICENCE: MIT
Language: Python3.10

"""

from time import sleep, time

from HedShell import (

    # shell functions.
    shell_input, 
    exit_shell,
    Command,
    EMPTY_COMMAND,
    Help, 
    # algorithm maps.
    hedshell_encode, 
    hedshell_decode,
    hedshell_hash,
    
    # enums.
    ENCODE, 
    DECODE,

    # docs.
    hashing_doc,  
    encode_decode_doc,
    DOC
)

Commands = {
    'EXIT':   exit_shell,
    'HELP':   Help,
    "HASH":   hedshell_hash,
    "DECODE": hedshell_decode,
    "ENCODE": hedshell_encode
}

def execute_command(command: Command) -> None:
    """ Executes the Command. """
    
    cmd, args = command[0], command[1]
    if not cmd in Commands:
        print("Command {} is not recognized.".format(cmd))      
        return
    
    Commands[cmd](args)

def run() -> None:
    """ Code that runs the shell. """
    while True:
        command = shell_input()
        if command != EMPTY_COMMAND: 
            execute_command(command)

def main():
    print()
    print(DOC) 
    run()

if __name__ == '__main__':
    main()

