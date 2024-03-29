
from .colors import (
    LIGHTYELLOW_EX,
    LIGHTBLUE_EX,
    BLUE,
    WHITE
)
from .types import Command

SALT_PATH     = "salt.bin"
EMPTY_COMMAND: Command = (str("E"), ["E"])
HEADER        = f"  { LIGHTYELLOW_EX }[*]{LIGHTBLUE_EX}[HED_SHELL]{BLUE} -> { WHITE }"
HELP_FLAG     = "--help"
CMDS = [
    "EXIT",     
    "HELP",     
    "ENCODE",   
    "DECODE",   
    "HASH",     
    "LOAD",     
    "DIGEST",   
    "FDECRYPT", 
    "FENCRYPT ",
    "ENCRYPT",  
    "DECRYPT",  
    "COMMANDS"
]


