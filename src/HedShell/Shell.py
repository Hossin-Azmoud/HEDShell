from colorama import Fore as f

Command       = type[str, list[str]] # str => command; list[str] => arguments.
EMPTY_COMMAND = ("E", ["E"])
HEADER        = f"  { f.YELLOW }[*][HED_SHELL] {f.CYAN} -> {f.WHITE}"

def shell_parse_command(self, cmd: str) -> Command: 
    """ Parses a command and returns the command and its args. """    

    if len(cmd) == 0: return EMPTY_COMMAND
    result = cmd.split(' ')
    if len(result) > 1:    
        command, args = result[0], result[1:] # named Unpacks for readablity purposes
        return (command, args)

    return (result[0], [])

def shell_input() -> Command: 
    """ Gets User input then returns a parsed command. """
    return shell_parse_command(input(HEADER))
       
def exit_shell() -> None:
	for i in ['.', '..', '...']:
		print(f"  Exiting{i}", end="\r")
		sleep(1)
	
    exit(0)





















