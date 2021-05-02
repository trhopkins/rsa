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
    return user

''' grab a keypair from a file '''
def getKeyPair(name):
    keyData = ""
    for line in fileinput.input(files = name):
        keyData += line
    keyData = keyData.split()
    user = RSA(name, int(keyData[0]), int(keyData[1]), int(keyData[2]))
    return user

''' given a file of encrypted blocks, return the plaintext '''
def decryptFile(filename, target):
    ciphertext = ""
    for line in fileinput.input(files = filename):
        ciphertext += line
    plaintext = target.decrypt(ciphertext)
    return plaintext

''' given a file of plaintext, return the encrypted blocks '''
def encryptFile(filename, target):
    plaintext = ""
    for line in fileinput.input(files = filename):
        plaintext += line
    ciphertext = target.encrypt(plaintext)
    return ciphertext

''' driver function '''
def main(): # toy example
    #genKeyPair("Travis")
    #genKeyPair("Mack")
    Travis = getKeyPair("Travis.txt")
    Mack = getKeyPair("Mack.txt")
    print(Travis.e)
    print(Travis.d)
    print(Travis.N)
    print()
    print(Mack.e)
    print(Mack.d)
    print(Mack.N)
    print()
    #Mack.encryptFile("email.txt", Travis)
    print(encryptFile("email.txt", Travis))
    #Travis.decryptFile("Mackemail.txt")

''' boilerplate '''
if __name__ == "__main__":
    main()

