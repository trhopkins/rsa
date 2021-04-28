#! /usr/bin/env python3

# Travis Hopkins and Mack Gromadski

import prime
#import sys, os # working with files and stdin

gen = prime.Prime()

''' Euclid's algorithm for finding modular inverses '''
def euclid(a, b):
    s = 0; oldS = 1
    t = 1; oldT = 0
    r = b; oldR = a
    while r != 0: # back substitution
        quot = oldR // r
        oldR, r = r, oldR - quot * r
        oldS, s = s, oldS - quot * s
        oldT, t = t, oldT - quot * t # only does two levels?
    return oldR, oldS, oldT # gcd, x, y

''' modular inverse, correcting with additive inverse '''
def modInv(a, b): # also by Euclid
    gcd, x, y = euclid(a, b)
    if x < 0: # negative residue requires modular additive inverse
        x += b
    return x

''' plaintext -> ciphertext '''
def encrypt(e, N, plaintext):
    ciphertext = "" # replace with list?
    for c in plaintext: # glorified substitution cipher; REPLACE
        m = ord(c)
        ciphertext += str(pow(m, e, N)) + " " # write yourself?
    return ciphertext

''' ciphertext -> plaintext '''
def decrypt(d, N, ciphertext):
    plaintext = "" # replace with list?
    blocks = ciphertext.split()
    for block in blocks: # each number = block
        c = int(block)
        plaintext += chr(pow(c, d, N))
    return plaintext

''' driver function '''
def main(): # toy example, no key generation yet
    p = 11
    q = 13
    N = p * q
    phiN = (p - 1) * (q - 1)
    e = 13
    d = modInv(e, phiN)
    msg = "Hello, world"
    ciphertext = encrypt(e, N, msg)
    plaintext = decrypt(d, N, ciphertext)
    print(ciphertext)
    print(plaintext)

''' boilerplate call to driver function '''
if __name__ == "__main__":
    main()

