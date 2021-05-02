#! /usr/bin/env python3

# Travis Hopkins and Mack Gromadzki

from rsa import RSA

bob = RSA()
alice = RSA()

''' driver function '''
def main(): # toy example
    msg = "Lorem ipsum dolor amset"
    ciphertext = alice.encrypt(msg, bob.public)
    plaintext = bob.decrypt(ciphertext)
    print(ciphertext)
    print(plaintext)

''' boilerplate '''
if __name__ == "__main__":
    main()

