#! /usr/bin/env python3

# Travis Hopkins and Mack Gromadski

import prime
#import sys, os # working with files and stdin

gen = prime.Prime()

''' Euclid's algorithm for finding multiplicative modular inverses '''
def multInv(a, b):
    s = 0; oldS = 1
    t = 1; oldT = 0
    r = b; oldR = a
    while r != 0: # back substitution, see slides
        quotient = oldR // r
        oldR, r = r, oldR - quotient * r
        oldS, s = s, oldS - quotient * s
        oldT, t = t, oldT - quotient * t
    if oldS < 0: # additive inverse if negative
        oldS += oldT
    return oldS # rename for clarity?

''' plaintext -> ciphertext '''
def encrypt(e, N, plaintext):
    ciphertext = []
    for c in plaintext: # glorified substitution cipher; FIX
        m = ord(c)
        ciphertext.append(str(pow(m, e, N)))
    return ciphertext

''' ciphertext -> plaintext '''
def decrypt(d, N, ciphertext):
    plaintext = ""
    for block in ciphertext: # each character = block; FIX
        c = int(block)
        plaintext += chr(pow(c, d, N))
    return plaintext

''' driver function '''
def main(): # toy example, no key generation yet
    p = 11
    q = 17
    N = p * q
    phiN = (p - 1) * (q - 1)
    e = 13
    d = multInv(e, phiN)
    # ed = 1 mod phiN, see book page 96
    msg = "Hello, world"
    ciphertext = encrypt(e, N, msg)
    plaintext = decrypt(d, N, ciphertext)
    print(ciphertext)
    print(plaintext)

''' boilerplate call to driver method '''
if __name__ == "__main__":
    main()

