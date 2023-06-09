from colorama import Fore as f
from time import sleep
from .colors import (
    RESET,
    GREEN,
    RED,
    YELLOW
)
from pathlib import Path
from .Algorithms import (
    hashing_doc,
    encode_decode_doc,
    ENCODE,
    DECODE,
    hashing,
    encoding
)

from .documentation import HELP, HED_SHELL_DOC 
from .constants import (
    EMPTY_COMMAND,
    HEADER,    
    HELP_FLAG
)

Command              = type[str, list[str]] # str => command; list[str] => arguments.
unexpected_arg_count = (lambda : print_error("unexpected number of arguments. please try again with the right amount."))
Commands = {}

def _reg_command(name, fn: callable) -> None: Commands[name] = fn
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

_reg_command("EXIT",   exit_shell) 

def Help(_: list[str]) -> None: print(HELP)

_reg_command("HELP",   Help) 

def print_result(s: str) -> None:
    print()
    print(f"  {GREEN}[RESULT]:{RESET}", s)
    print()

def print_info(s: str) -> None:
    print()
    print(f"  {GREEN}[!][INFO] {RESET}", s)
    print()

def print_error(e: str) -> None:
    print()
    print(f"  {RED}[ERROR]:{RESET}", e)
    print()

def print_documentation():
    print()
    print(HED_SHELL_DOC)

def print_syntax(t: str) -> None:
    print()
    print(f"  {YELLOW}[SYNTAX]:{RESET}", t)
    print()

def hedshell_encode(args: list[str]) -> None: 
        
    if len(args) == 0:
        print_syntax(encode_decode_doc[ENCODE])
        return

    if len(args) < 2:
        
        if args[0] == HELP_FLAG:
            print_syntax(encode_decode_doc[ENCODE])
            return

        unexpected_arg_count()
        return

    text, algorithm = args[0], args[1].upper()
    if not algorithm in encoding:
        
        print_error("  [ERROR] %s Algorithms was not found!" % algorithm)
        print_syntax(encode_decode_doc[ENCODE])
        return

    fn = encoding[algorithm][ENCODE]
    if isinstance(text, str): 
        text = text.encode()
    
    print_result(fn(text).decode())

_reg_command("ENCODE", hedshell_encode) 

def hedshell_decode(args: list[str]) -> None:
    
    if len(args) == 0:
        print_syntax(encode_decode_doc[DECODE])
        return

    if len(args) < 2:
        
        if args[0] == HELP_FLAG:
            print_syntax(encode_decode_doc[DECODE])
            return

        unexpected_arg_count()
        return   

    text, algorithm = args[0], args[1].upper()
    
    if not algorithm in encoding:
        
        
        print_error("  [ERROR] %s Algorithms was not found!" % algorithm)
        print_syntax(encode_decode_doc[DECODE])
        return
    
    fn = encoding[algorithm][DECODE]
    if isinstance(text, str): 
        text = text.encode()
    
    print_result(fn(text).decode())

_reg_command("DECODE", hedshell_decode) 

def hedshell_hash(args: list[str]) -> None:
    
    if len(args) == 0:
        print_syntax(hashing_doc)
        return

    if len(args) < 2:
        
        if args[0] == HELP_FLAG:
            print_syntax(hashing_doc)
            return

        unexpected_arg_count()
        return   

    text, algorithm = args[0], args[1].upper()
    if not algorithm in hashing:
        
        print_error("  [ERROR] %s Algorithms was not found!" % algorithm)
        print_syntax(hashing_doc)
        return

    if isinstance(text, str) : text = text.encode()
    fn = hashing[algorithm]
    print_result(fn(text).hexdigest())

_reg_command("HASH",   hedshell_hash) 

def execute_command(command: Command) -> None:
    """ Executes the Command. """
    
    cmd, args = command[0], command[1]
    if not cmd in Commands:
        print_error("Command {} is not recognized.".format(cmd))      
        return
    
    Commands[cmd](args)


def load_commands(args: list[str]):
    if len(args) == 0:
        print_syntax("load FILENAME")
        return
    
    file     = Path(args[0])
    if not file.exists():
        print_error("  [ERROR] %s does not exist" % file)
        return
        
    lines = file.read_text().split("\n")
    if len(lines) == 0:
        print_info("EMPTY COMMAND FILE.")
        return
    
    # TODO: There is a better way of doing this... 
    all_      = len(lines)
    proccessed = 0

    for command in lines:
        print_info(f"executing command: { command }  {proccessed}/{all_}")
        c = shell_parse_command(command)
        execute_command(c)
        proccessed += 1

_reg_command("LOAD",   load_commands)

