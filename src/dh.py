#! usr/bin/env python3

# Diffie-Hellman key exchange code
# Travis Hopkins and Mack Gromadzki

from prime import Prime

class DH:
    ''' boilerplate '''
    def __init__(self, g, secret, p): # g and p are public
        self.g = g
        self.secret = secret
        self.p = p
        self.sharedSecret = None # g^secret mod p

    ''' modular exponent function. Still slower than builtin pow :( '''
    def expMod(self, b, e, m): # base^exponent mod modulus
        if e == 1:
            return b % m
        x = self.expMod(b, e>>1, m)
        x = (x * x) % m
        if e & 1 == 1: # if odd shortcut
            x = (x * b) % m
        return x # see SICP page 56

    ''' g^a mod p '''
    def generatePartialSecret(self):
        partialSecret = self.expMod(self.g, self.secret, self.p)
        return partialSecret

    ''' g^a mod p '''
    def generateSharedSecret(self, otherPartialKey): # g^b mod p
        self.sharedSecret = self.expMod(otherPartialKey, self.secret, self.p)
        return self.sharedSecret

    ''' encrypt message with fullKey '''
    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext: # simple obfuscation like substitution
            ciphertext += chr(ord(char) + self.fullKey)
        return ciphertext

    ''' decrypt message with fullKey '''
    def decrypt(self, ciphertext):
        plaintext = ""
        for char in ciphertext: # simple obfuscation like substitution
            plaintext += chr(ord(char) - self.fullKey)
        return plaintext

def main():
    # insert test cases here, later?
    pass

''' boilerplate '''
if __name__ == "__main__":
    main()

