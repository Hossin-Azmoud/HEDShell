from HedShell import run
from random import randint

import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def write_tst_file(fn: str, capacity: int) -> None:
    with open(fn, "w+") as fp:
        for i in range(0, capacity * 1024): 
            fp.write(str(randint(0, 10)))


def main():
    # run()
    # write_tst_file("file.test", 2)

    password = b"password"

    salt = os.urandom(16)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    
    f = Fernet(key)

    token = f.encrypt(b"Secret message!")
    data  = f.decrypt(token)

    print(data)
    print(token)


if __name__ == '__main__':
    main()

