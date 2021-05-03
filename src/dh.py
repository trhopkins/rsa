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

    ''' g^a mod p '''
    def generatePartialSecret(self):
        partialSecret = (self.g ** self.secret) % self.p
        return partialSecret

    ''' g^a mod p '''
    def generateSharedSecret(self, otherPartialKey): # g^b mod p
        self.sharedSecret = (otherPartialKey ** self.secret) % self.p
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

