from .Shell import parse_command, shell_input, EMPTY_COMMAND, Command
from .UtilFuncs import LoadConfig
from .Algorithms import *

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

HELP = """

	To encode/Decode:
		Encode/Decode <Text> <Algorithm>
		Encode/Decode only for help.
	To hash:
		Hash <Text> <Algorithm>
		Hash only for help.

"""


