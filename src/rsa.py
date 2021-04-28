#! /usr/bin/env python3

# Travis Hopkins and Mack Gromadski

import prime
#import sys, os # working with files and stdin

gen = prime.Prime()

''' modular inverse '''
def modInv():
    pass

''' plaintext -> ciphertext '''
def encrypt(e, N, plaintext):
    pass

''' ciphertext -> plaintext '''
def decrypt(d, N, ciphertext):
    pass

''' driver function '''
def main():
    p = 11
    q = 13
    N = p * q
    phiN = (p - 1) * (q - 1)
    e = 13
    #d = modInv(e, phiN)

''' boilerplate call to driver function '''
if __name__ == "__main__":
    main()

