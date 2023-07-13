from os import urandom
from time import sleep
from .colors import (
    RESET,
    GREEN,
    RED,
    YELLOW
)
from pathlib import Path
from .algorithms import (
    hashing_doc,
    encode_decode_doc,
    ENCODE,
    DECODE,
    hashing,
    encoding
)
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from .documentation import HELP, HED_SHELL_DOC 
from .constants import (
    EMPTY_COMMAND,
    HEADER,    
    HELP_FLAG
)

console_lock         = False
SALT_PATH            = "salt.bin"
Command              = type[str, list[str]] # str => command; list[str] => arguments.
unexpected_arg_count = (lambda : print_error("unexpected number of arguments. please try again with the right amount."))
Commands = {}

DQUOTE   = "\""
SQUOTE   = "\'"


def lock_console():
    console_lock = True

def unlock_console():
    console_lock = False 

def tokenize_cmd(cmd: str) -> list[str] | None:
    length     = len(cmd)
    arg_buffer = "" 
    idx        = 0
    list_      = []
    l_size     = 0

    while idx < length:
        if cmd[idx] == ' ':
            if len(arg_buffer) > 0:
                list_.append(arg_buffer)
                arg_buffer = ""
                l_size += 1

            idx += 1    
            continue

        if cmd[idx] == DQUOTE:

            if len(arg_buffer) > 0:
                print_error("non-closed quote. in idx %i" % idx)
                return

            idx += 1

            while idx < length:
                
                if cmd[idx] == DQUOTE:
                    break

                arg_buffer += cmd[idx]
                idx += 1

            if idx == length:
                print_error("reached the tail of the buffer but closing quote was not found.")
                return

            if cmd[idx] == DQUOTE:
                if idx == length - 1:
                    
                    if len(arg_buffer) > 0:
                        list_.append(arg_buffer) 
                    
                    arg_buffer = ""
                    l_size    += 1
                    idx += 1
                    continue
 
                if cmd[idx + 1] == ' ':
                    if len(arg_buffer) > 0:
                        list_.append(arg_buffer) 

                    arg_buffer = ""
                    l_size    += 1
                    idx += 2
                    continue
                
                print_error("miformating of the commands, please check ur input.")
                return

            print_info("UNREACHEDBALE WAS REACHED! BUG IN THE CODE")

        if cmd[idx] == SQUOTE:
            if len(arg_buffer) > 0:
                print_error("non-closed quote. in idx %i" % idx)
                return

            idx += 1
            
            while (idx < length):

                if cmd[idx] == SQUOTE:
                    break
                
                arg_buffer += cmd[idx]
                idx += 1

            if idx == length:
                print_error("reached the tail of the buffer but closing quote was not found.")
                return

            if cmd[idx] == SQUOTE:
                if idx == length - 1:    
                    if len(arg_buffer) > 0:
                        list_.append(arg_buffer) 
                    
                    arg_buffer = ""
                    l_size    += 1
                    idx += 1
                    continue
 
                if cmd[idx + 1] == ' ':
                    if len(arg_buffer) > 0:
                        list_.append(arg_buffer) 

                    arg_buffer = ""
                    l_size    += 1
                    idx += 2
                    continue
                
                print_error("miformating of the commands, please check ur input.")
                return

            print_info("UNREACHEDBALE WAS REACHED! BUG IN THE CODE")

        arg_buffer += cmd[idx]
        idx += 1
    
    if len(arg_buffer) > 0:
        list_.append(arg_buffer)

    return list_ 

def _reg_command(name: str, fn: callable) -> None: 
    Commands[name] = fn

def shell_parse_command(cmd: str) -> Command: 
    """ Parses a command and returns the command and its args. """    
    cmd = cmd.strip() # Clears the spaces.
    if len(cmd) == 0: return EMPTY_COMMAND
    result = tokenize_cmd(cmd)
    if result == None: return EMPTY_COMMAND

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

def get_salt() -> bytes:
    f = Path(SALT_PATH)

    if not f.exists():
        salt = urandom(16)
        f.write_bytes(salt)
        return salt

    return f.read_bytes()

def Help(_: list[str]) -> None: print(HELP)

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
    return fn(text).decode()

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
    return fn(text).decode()

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
    return fn(text).hexdigest()

def not_implemented_yet():
    print("THIS FUNCTION IS NOT IMPLEMENTED YET!")

def fernet_encrypt(args: list[str]):
    # encrypt fernet "data..." "pwd"
    if len(args) < 2:
        print_syntax("encrypt <algorithm> <data> <password>")
        return

    #alg  = args[0] dissmissed for now.
    data = args[1]
    
    if len(args) == 2:
        pwd = input("please supply a password: ")
        while len(pwd) < 6:
            pwd = input("very short, please supply a password (more than 6 chars long.): ")
    else:
        pwd = args[2]
    
    salt = get_salt()
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )

    key = urlsafe_b64encode(kdf.derive(pwd.encode()))
    f = Fernet(key)
    encrypted = f.encrypt(data.encode())

    if not console_lock:
        print(encrypted)
        return

    return encrypted


def fernet_decrypt(args: list[str]):
    # decrypt fernet "encypted data in base64..." "password"
    if len(args) < 2:
        print_syntax("decrypt <algorithm> <data> <password>")
        return

    #alg  = args[0] dissmissed for now.
    data = args[1]
    
    if len(args) == 2:
        pwd = input("please supply a password: ")
        while len(pwd) < 6:
            pwd = input("very short, please supply a password (more than 6 chars long.): ")
    else:
        pwd = args[2]

    salt = get_salt() 
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )

    k   = urlsafe_b64encode(kdf.derive(pwd.encode()))
    f   = Fernet(k)
    decrypted = (f.decrypt(token))

    if not console_lock:
        print(decrypted)
        return

    return decrypted

def fernet_encryptf(args: list[str]):
    # fencrypt fernet fname "password" 
    # lock_console()
    # encrypted    = fernet_encrypt(args[1:])
    # lock_console()
    not_implemented_yet()

def fernet_decryptf(args: list[str]):
    # fdecrypt fernet fname "password"
    not_implemented_yet()

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
        
    lines = [
        i 
        for i in file.read_text().split("\n") 
        if (i.strip() and i.strip()[0]) != "#"
    ]

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

def digest_file(args: list[str]):
    """ digest -e | -d | -h  """
    if len(args) < 2:
        print_syntax("digest [encoode | decode | hash] <algorithm> FILENAME OUTPUT_FN")
        return
    
    op     = args[0]
    algo   = args[1]
    file   = Path(args[2])
    
    if not file.exists():
        print_error("  [ERROR] %s does not exist" % file)
        return

    bytes_ = file.read_bytes()
    
    if len(bytes_) > 0: 
        data = Commands[op.upper()]([bytes_, algo])
        fn   = f"{file}.out"

        if len(args) == 4:
            fn = args[3]
        
        print_result(f"The output of this command will be written in: { fn }")
        with open(file, "w+") as fp: 
            fp.write(data)

        print_result(f"WROTE TO { fn }")

# ADD Commands.
_reg_command("EXIT",   exit_shell)
_reg_command("HELP",   Help) 
_reg_command("ENCODE", hedshell_encode) 
_reg_command("DECODE", hedshell_decode) 
_reg_command("HASH",   hedshell_hash) 
_reg_command("LOAD",   load_commands)
_reg_command("DIGEST", digest_file)
_reg_command("FDECRYPT", fernet_decryptf)
_reg_command("FENCRYPT ", fernet_encryptf) 
_reg_command("ENCRYPT",   fernet_encrypt) 
_reg_command("DECRYPT",   fernet_decrypt)

