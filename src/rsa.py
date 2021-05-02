#! /usr/bin/env python3

# Travis Hopkins and Mack Gromadzki

from prime import Prime
from random import randint

class RSA:
    ''' boilerplate '''
    def __init__(self): # TODO: extend to include optional e, d, N
        self.keyGen = Prime()
        self.genPQ()
        self.genKeyPair()

    ''' generate two primes, basis for e, d, N, etc. '''
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

    ''' modular exponent function. Still slower than builtin pow :( '''
    def expMod(self, b, e, m): # base^exponent mod modulus
        if e == 1:
            return b % m
        x = self.expMod(b, e>>1, m)
        x = (x * x) % m
        if e & 1 == 1: # if odd shortcut
            x = (x * b) % m
        return x # see SICP page 56

    ''' encrypt block of 8 characters '''
    def encryptBlock(self, plaintext, public=None):
        if public == None:
            public = self.public
        e, N = public[0], public[1]
        ciphertext = ""
        for char in plaintext:
            ciphertext += "{:0>2x}".format(ord(char))
        ciphertext = "{:0>2x}".format(self.expMod(int(ciphertext, 16), e, N))
        return ciphertext

    ''' decrypt block of 8 characters '''
    def decryptBlock(self, ciphertext, private=None):
        if private == None:
            private = self.private
        d, N = private[0], private[1]
        ciphertext = "{:0>2x}".format(self.expMod(int(ciphertext, 16), d, N))
        hex = [(ciphertext[i:i+2]) for i in range(0, len(ciphertext), 2)]
        plaintext = ""
        for char in hex:
            plaintext += chr(int(char, 16))
        return plaintext

    ''' encrypt message by composing into blocks '''
    def encrypt(self, plaintext, public=None):
        if public == None: 
            public = self.public # default to own key
        ciphertext = ""
        # thank you Automate the Boring Stuff for this bit of shorthand
        blocks = [(plaintext[i:i+8]) for i in range(0, len(plaintext), 8)]
        while len(blocks[-1]) != 8:
            blocks[-1] += " " # uniform block lengths
        for block in blocks:
            ciphertext += self.encryptBlock(block, public)
            ciphertext += "\n" # delimiter can be "\n" or " "
        return(ciphertext)

    ''' decrypt message composed of blocks '''
    def decrypt(self, ciphertext, private=None):
        if private == None:
            private = self.private # default to own key
        plaintext = ""
        blocks = ciphertext.split()
        for block in blocks: # may be long message
            plaintext += self.decryptBlock(block, private)
        return plaintext

'''
alice = RSA()
message = alice.encrypt("Hello, world! My name is Travis Hopkins.")
print(message)
print(alice.decrypt(message))
'''

