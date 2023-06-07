from .core import (
    shell_input, 
    EMPTY_COMMAND, 
    HELP_FLAG,
    Command, 
    exit_shell, 
    print_result, 
    print_error, 
    print_syntax,
    Help, 
    DOC
)

from .Algorithms import *
unexpected_arg_count = (lambda : print_error("unexpected number of arguments. please try again with the right amount."))

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

