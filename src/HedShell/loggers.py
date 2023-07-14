from .constants import CMDS
from .documentation import HELP, HED_SHELL_DOC
from .colors import (
    RESET,
    RED,
    YELLOW,
    GREEN
)

def print_cmds(_: list[str]):

    for i, command in enumerate(CMDS):
        print("  #{} {}".format(
            i,
            command
        ))

def not_implemented_yet(): print("THIS FUNCTION IS NOT IMPLEMENTED YET!")

def print_Help(_: list[str]) -> None: 
    print()
    print(HELP)
    print()

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

