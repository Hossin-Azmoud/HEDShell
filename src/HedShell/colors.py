from colorama import Fore

BLACK = Fore.BLACK
BLUE = Fore.BLUE
CYAN = Fore.CYAN
GREEN = Fore.GREEN
LIGHTBLACK_EX = Fore.LIGHTBLACK_EX
LIGHTBLUE_EX = Fore.LIGHTBLUE_EX
LIGHTCYAN_EX = Fore.LIGHTCYAN_EX
LIGHTGREEN_EX = Fore.LIGHTGREEN_EX
LIGHTMAGENTA_EX = Fore.LIGHTMAGENTA_EX
LIGHTRED_EX = Fore.LIGHTRED_EX
LIGHTWHITE_EX = Fore.LIGHTWHITE_EX
LIGHTYELLOW_EX = Fore.LIGHTYELLOW_EX
MAGENTA = Fore.MAGENTA
RED = Fore.RED
RESET = Fore.RESET
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW


if __name__ == "__main__":
	for i in dir(Fore):
		if i.startswith('__'):
			pass
		else:
			print(f'{eval(i)}{i} = Fore.{i}')
	print(f"""
{GREEN}successfully Installed in Home
{LIGHTMAGENTA_EX}Now you can try to add to PATH so you can access the shell from wherever you want!
                """)
	print(RESET)

print(RESET)
