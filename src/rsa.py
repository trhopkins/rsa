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

    ''' plaintext -> ciphertext '''
    def encrypt(self, plaintext, public=None):
        if public == None:
            public = self.public
        ciphertext = []
        for c in plaintext: # glorified substitution cipher; FIX
            m = ord(c)
            ciphertext.append(str(self.expMod(m, public[0], public[1])))
        return ciphertext

    ''' ciphertext -> plaintext '''
    def decrypt(self, ciphertext, private=None):
        if private == None:
            private = self.private
        plaintext = ""
        for block in ciphertext: # each character = block; FIX
            c = int(block)
            plaintext += chr(pow(c, private[0], private[1])) # faster
            #plaintext += chr(self.expMod(c, private[0], private[1]))
        return plaintext

    ''' block-based encryption method '''
    def encryptBlock(self, plaintext, public=None):
        if public == None:
            public = self.public
        blob = ""
        for char in plaintext:
            blob += "{:0>2x}".format(ord(char))
        ciphertext = str(self.expMod(int(blob, 16), public[0], public[1]))
        return ciphertext

    ''' block-based decryption method '''
    def decryptBlock(self, ciphertext, private=None):
        if private == None:
            private = self.private
        blob = "{:0>2x}".format(self.expMod(int(ciphertext), private[0], private[1]))
        hex = [(blob[i:i+2]) for i in range(0, len(blob), 2)]
        plaintext = ""
        for char in hex:
            plaintext += chr(int(char, 16))
        return plaintext

'''
alice = RSA()
message = "Hello"
ciphertext = alice.encryptBlock(message)
plaintext = alice.decryptBlock(ciphertext)
print(plaintext)
'''

