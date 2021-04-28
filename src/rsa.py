#! /usr/bin/env python3

# Travis Hopkins and Mack Gromadski

from prime import Prime
from random import randint

class RSA:
    ''' boilerplate '''
    def __init__(self): # TODO: extend to include optional e, d, N
        self.keyGen = Prime()
        self.genPQ()
        self.genKeyPair()

    ''' generate two primes, basis for N, e, d, etc. '''
    def genPQ(self):
        self.p, self.q = self.keyGen.genPrimes()

    ''' generate private key, public key, and N '''
    def genKeyPair(self):
        N = self.p * self.q
        phiN = (self.p - 1) * (self.q - 1)
        e = randint(2, phiN)
        g = self.gcd(e, phiN)
        d = -1
        while (not self.isCoPrime(e, phiN)) or d < 1:
            e = randint(2, phiN)
            d = self.multInv(e, phiN)
        self.e = e; self.d = d; self.N = N
        self.private = (d, N); self.public = (e, N);

    ''' Euclid's algorithm for finding greatest common denominators '''
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    ''' check if numbers are relatively prime '''
    def isCoPrime(self, a, b):
        return self.gcd(a, b) == 1

    ''' Euclid's algorithm for finding multiplicative inverses '''
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

    ''' modular exponent function. Still slower than builtin pow :( '''
    def expMod(self, a, b, m): # a^b mod m
        if b == 1:
            return a % m
        tmp = self.expMod(a, b>>1, m)
        tmp = (tmp * tmp) % m
        if b & 1 == 1: # if odd shortcut
            tmp = (tmp * a) % m
        return tmp # see SICP page 56

    ''' plaintext -> ciphertext '''
    def encrypt(self, plaintext, public=None):
        if public == None:
            public = self.public
        ciphertext = []
        for c in plaintext: # glorified substitution cipher; FIX
            m = ord(c)
            ciphertext.append(str(pow(m, public[0], public[1])))
            #ciphertext.append(str(self.expMod(m, public[0], public[1])))
        return ciphertext

    ''' ciphertext -> plaintext '''
    def decrypt(self, ciphertext, private=None):
        if private == None:
            private = self.private
        plaintext = ""
        for block in ciphertext: # each character = block; FIX
            c = int(block)
            plaintext += chr(pow(c, private[0], private[1]))
            #plaintext += chr(self.expMod(c, private[0], private[1]))
        return plaintext

