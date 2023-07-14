from collections.abc import Callable
DQUOTE   = "\""
SQUOTE   = "\'"
func = Callable[[str], None]

def tokenize_cmd(cmd: str, print_info: func, print_error: func) -> list[ str ] | None:
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

