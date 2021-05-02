#! /usr/bin/env python3

# Travis Hopkins and Mack Gromadzki

from rsa import RSA # encryption/decryption
import fileinput # file IO
import sys # command line arguments

''' generate a keypair for a user '''
def genKeyPair(name):
    user = RSA(name)
    #print(user.e)
    #print(user.d)
    #print(user.N)
    return user # consider writing to file instead?

''' grab a keypair from a file '''
def getKeyPair(name): # Travis.txt, Mack.txt
    keyData = ""
    for line in fileinput.input(files = name): # lines = numbers
        keyData += line
    e, d, N = keyData.split()
    user = RSA(name, int(e), int(d), int(N))
    return user

''' given a file of encrypted blocks, return the plaintext '''
def decryptFile(filename, target):
    ciphertext = ""
    for line in fileinput.input(files = filename): # lines = blocks
        ciphertext += str.rstrip(line)
    plaintext = target.decrypt(ciphertext)
    return plaintext

''' given a file of plaintext, return the encrypted blocks '''
def encryptFile(filename, target):
    plaintext = ""
    for line in fileinput.input(files = filename):
        plaintext += str.rstrip(line)
    ciphertext = target.encrypt(plaintext)
    enc = open("enc.txt", "w")
    enc.write(ciphertext)
    enc.close()
    #return ciphertext

''' driver function '''
def main(): # toy example
    '''
    operation = sys.argv[1]
    target = sys.argv[2]
    Travis = getKeyPair("Travis.txt")
    Mack = getKeyPair("Mack.txt")
    if operation == "encrypt":
        ciphertext = Travis.encrypt(sys.argv[3:], mack.public)
    message = sys.argv[1]
    encryptFile(message, Travis)
    print(decryptFile("enc.txt", Travis))
    #cipher = Mack.encrypt("Hello, world! This is Travis Hopkins!")
    #plain = Mack.decrypt(cipher)
    #print(plain)
    '''
    Travis = getKeyPair("Travis.txt")
    Mack = getKeyPair("Mack.txt")
    msg = "Hello"
    sig = Travis.encryptBlock(msg)
    print(Travis.decryptBlock(sig))

''' boilerplate '''
if __name__ == "__main__":
    main()

