from HedShell import run
from random import randint

def write_tst_file(fn: str, capacity: int) -> None:
    with open(fn, "w+") as fp:
        for i in range(0, capacity * 1024): 
            fp.write(str(randint(0, 10)))


def main():
    run()

if __name__ == '__main__':
    main()
