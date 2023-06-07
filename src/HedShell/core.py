from colorama import Fore as f
from time import sleep

HELP = """

    To encode/Decode:
        Encode/Decode <Text> <Algorithm>
        Encode/Decode only for help.
    
    To hash:
        Hash <Text> <Algorithm>
        Hash only for help.

"""

DOC = f"""{f.YELLOW}

    Author: Hossin azmoud (Moody0101)
    Date: 10/18/2022
    LICENCE: MIT
    Language: {f.CYAN}Python3.10 {f.YELLOW}
    Descripion: A tool to hash, encode, decode text.
    command: hash, encode, decode, help, exit
    Usage: 
        To encode/Decode:
            Encode/Decode <Text> <Algorithm>
            Encode/Decode only for help.
        To hash:
            Hash <Text> <Algorithm>
            Hash only for help.
"""

Command       = type[str, list[str]] # str => command; list[str] => arguments.
EMPTY_COMMAND = ("E", ["E"])
HEADER        = f"  { f.YELLOW }[*][HED_SHELL] {f.CYAN} -> {f.WHITE}"
HELP_FLAG = "--help"

def shell_parse_command(cmd: str) -> Command: 
    """ Parses a command and returns the command and its args. """    
    
    cmd = cmd.strip() # Clears the spaces.

    if len(cmd) == 0: return EMPTY_COMMAND
    
    result = [
        i 
        for i in cmd.split(' ') 
        if i # check if it is a valid string.
    ]
    
    if len(result) > 1:    
        command, args = result[0], result[1:] # named Unpacks for readablity purposes
        return (command.upper(), args)

    return (result[0].upper(), [])

def shell_input() -> Command: 
    """ Gets User input then returns a parsed command. """
    return shell_parse_command(input(HEADER))
       
def exit_shell(_: list[str]) -> None:
    """ Exits the shell with 0 exit code. """
    
    for i in ['.', '..', '...']:
        print(f"  Exiting{i}", end="\r")
        sleep(.1)
    
    exit(0)

def Help(_: list[str]) -> None: print(HELP)

def print_result(s: str) -> None:
    print()
    print(f"  {f.GREEN}[RESULT]:{f.RESET}", s)
    print()


def print_error(e: str) -> None:
    print()
    print(f"  {f.RED}[ERROR]:{f.RESET}", e)
    print()

def print_syntax(t: str) -> None:
    print()
    print(f"  {f.YELLOW}[SYNTAX]:{f.RESET}", t)
    print()


