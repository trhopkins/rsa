# RSA implementation
# Travis Hopkins and Mack Gromadzki


from prime import Prime # key generation
from random import randint # key generation

class RSA:
    ''' boilerplate '''
    def __init__(self, name, e=None, d=None, N=None):
        self.name = name
        self.keyGen = Prime()
        if e != None and d != None and N != None:
            self.e = e
            self.d = d
            self.N = N
            self.public = (self.e, self.N)
            self.private = (self.d, self.N)
        else:
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
        return self.gcd(a, b) == 1 # thanks Fermat

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

    ''' encrypt block of 8 characters base64 '''
    def encryptBlock(self, plaintext, public=None):
        if public == None:
            public = self.public
        e, N = public[0], public[1]
        ciphertext = 0
        for char in plaintext:
            ciphertext <<= 7 # 2**7 possible ASCII characters
            ciphertext += ord(char) # each 7 bits = 1 character
        ciphertext = self.expMod(ciphertext, e, N)
        return str(ciphertext)

    ''' decrypt block of 8 characters '''
    def decryptBlock(self, ciphertext, private=None):
        ciphertext = int(ciphertext)
        if private == None:
            private = self.private
        d, N = private[0], private[1]
        numPlain = self.expMod(ciphertext, d, N)
        plaintext = ""
        while numPlain:
            plaintext += chr(numPlain % 128) # ASCII table translation
            numPlain >>= 7 # move down stack, 7 bits at a time
        return plaintext[::-1] # stack-based blocks output in reverse

    ''' sign block of 8 characters '''
    def signBlock(self, plaintext, private=None):
        if private == None:
            private = self.private
        d, N = private[0], private[1]
        signature = 0
        for char in plaintext:
            signature <<= 7
            signature += ord(char)
        signature = self.expMod(signature, d, N) # encrypt with public
        return str(signature)

    ''' check block signature '''
    def checkBlockSignature(self, signature, public=None):
        signature = int(signature)
        if public == None:
            public = self.public
        d, N = public[0], public[1]
        numPlain = self.expMod(signature, d, N) # decrypt with private
        plaintext = ""
        while numPlain:
            plaintext += chr(numPlain % 128)
            numPlain >>= 7
        return plaintext[::-1] # reversed due to the way >> works

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
        return ciphertext

    ''' decrypt message composed of blocks '''
    def decrypt(self, ciphertext, private=None):
        if private == None:
            private = self.private # default to own key
        plaintext = ""
        blocks = ciphertext.split()
        for block in blocks: # may be long message
            plaintext += self.decryptBlock(block, private)
        return plaintext

    def sign(self, plaintext, private=None):
        if private == None:
            private = self.private # default to own key
        signature = ""
        # thank you Automate the Boring Stuff for this bit of shorthand
        blocks = [(plaintext[i:i+8]) for i in range(0, len(plaintext), 8)]
        while len(blocks[-1]) != 8:
            blocks[-1] += " " # uniform block lengths
        for block in blocks:
            signature += str(self.signBlock(block, private))
            signature += "\n" # delimiter can be "\n" or " "
        return(signature)

    def checkSignature(self, signature, public=None):
        if public == None:
            public = self.public # default to own key
        plaintext = ""
        blocks = signature.split()
        for block in blocks: # may be long message
            plaintext += self.decryptBlock(int(block), public)
        return plaintext

