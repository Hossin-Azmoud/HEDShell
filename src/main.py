
"""

Author: Hossin azmoud (Moody0101)
Date: 10/18/2022
LICENCE: MIT
Language: Python3.10

"""

from time import sleep, time
from colorama import Fore as f

from HedShell import (
    parse_command, 
    shell_input, 
    EMPTY_COMMAND
	ENCODING,
	HASHING,
	EncodingManager, # EncodingManager(Func: callable, s: str | bytes, Op: int)
	ENCODE, 
	DECODE,
	Hasher # Hasher(HashingFunc: callable, s: str | bytes) -> str: 
)


class Interface:
	""" An interface that handles user interactions with the shell program """
	
	def __init__(self) -> None:
		# Shell initializer
		self.shell = Shell()
		
		
		self.DefaultCommands = {
			'EXIT': self.Exit,
			'HELP': self.Help,
			"HASH": self.hashDoc,
			"DECODE": self.DeDoc,
			"ENCODE": self.EnDoc
		}

		self.Commands = {
			"HASH": self.hashVal,
			"DECODE": self.Decode,
			"ENCODE": self.Encode
		}

	def hashDoc(self):
		""" Displays doc for hashing """
		return HASHING["Doc"] 

	def DeDoc(self):
		""" Displays doc for decoding """
		return ENCODING["Doc"][DECODE]

	def EnDoc(self):
		""" Displays doc for encoding """
		return ENCODING["Doc"][ENCODE]

	def Encode(self, Text, EncoderName):
		if EncoderName.upper().strip() not in ENCODING.keys():
			print()
			print(f"  False algorithm name, {EncoderName}")
			print("  you can only use from this list:")
			for i in ENCODING.keys():
				print("    %s", i)
			return

		# Get Encoder function
		func_ = ENCODING[EncoderName.upper().strip()][ENCODE]
		# Map the value
		encode = EncodingManager(func_, ENCODE)
		# return the value
		return encode(Text)

	def Decode(self, Text, DecoderName):
		if DecoderName.upper().strip() not in ENCODING.keys():
			print()
			print(f"  False algorithm name, {DecoderName}")
			print("  you can only use from this list:")
			for i in ENCODING.keys():
				print("    %s", i)
			return

		# Get Encoder function
		func_ = ENCODING[DecoderName.upper().strip()][DECODE]
		# Map the value
		decode = EncodingManager(func_, DECODE)
		# return the value
		return decode(Text)

	def hashVal(self, Text, HasherName):
		if HasherName.upper().strip() not in HASHING.keys():
			print()
			print(f"  False algorithm name, {DecoderName}")
			print("  you can only use from this list:")
			for i in HASHING.keys():
				print("    %s", i)
			return

		return Hasher(HASHING[HasherName.upper().strip()], Text)


def execute(command: Command) -> None:
    """ Executes the Command. """
    
    if command.CMD in self.DefaultCommands.keys():
        
        if len(command.argv) > 0:
            print(self.Commands[command.CMD](*command.argv))
        else:
            print(self.DefaultCommands[command.CMD]())
    elif command.CMD in self.Commands.keys():
        if len(command.argv) > 0:
            print(self.Commands[command.CMD](*command.argv))
        else:
            print(self.Commands[command.CMD]())

def run() -> None:
    while True:
        command = shell_input()
        if command != EMPTY_COMMAND: self.execute(self.command)
        execute_command(command)

def main():
    print()
	print(DOC)

    Interface_ = Interface()
	Interface_.run()


if __name__ == '__main__':
	main()

