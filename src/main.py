from HedShell import run
from random import randint

def write_tst_file(fn: str, capacity: int) -> None:
    print("written: {}".format(capacity * 1024))
    with open(fn, "w+") as fp:
        for i in range(0, capacity * 1024): 
            fp.write(str(randint(0, 9)))


def main():
    # write_tst_file("Hello", 23) 01: 40 end: 65
    run()
    
if __name__ == '__main__':
    main()
