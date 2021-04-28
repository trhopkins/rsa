# Travis Hopkins and Mack Gromadski

import prime
from random import randint

class RSA:
    ''' boilerplate '''
    def __init__(self):
        self.keyGen = prime.Prime()

    ''' generate two primes, basis for N, e, d, etc. '''
    def genPQ(self):
        p, q = self.keyGen.genPrimes()
        return p, q

    ''' generate private key, public key, and N '''
    def genKeyPair(self, p, q):
        N = p * q
        phiN = (p - 1) * (q - 1)
        e = randint(2, phiN)
        g = self.gcd(e, phiN)
        d = -1
        while (not self.isCoPrime(e, phiN)) or d < 1:
            e = randint(2, phiN)
            d = self.multInv(e, phiN)
        # public key, private key. Set internal variables in __init__?
        return e, d, N

    ''' Euclid's algorithm for finding greatest common denominators '''
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    ''' check if numbers are relatively prime '''
    def isCoPrime(self, a, b):
        return self.gcd(a, b) == 1

    ''' Euclid's algorithm for finding multiplicative modular inverses '''
    def multInv(self, a, b): # TODO: fix negative private key bugs
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

