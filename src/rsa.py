# Travis Hopkins and Mack Gromadski

import prime

class RSA:
    gen = prime.Prime()

    ''' boilerplate '''
    def __init__(self):
        pass

    ''' Euclid's algorithm for finding greatest common denominators '''
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    ''' Euclid's algorithm for finding multiplicative modular inverses '''
    def multInv(self, a, b):
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
    def encrypt(self, e, N, plaintext):
        ciphertext = []
        for c in plaintext: # glorified substitution cipher; FIX
            m = ord(c)
            ciphertext.append(str(pow(m, e, N)))
        return ciphertext

    ''' ciphertext -> plaintext '''
    def decrypt(self, d, N, ciphertext):
        plaintext = ""
        for block in ciphertext: # each character = block; FIX
            c = int(block)
            plaintext += chr(pow(c, d, N))
        return plaintext

