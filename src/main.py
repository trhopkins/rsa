#! /usr/bin/env python3

# Travis Hopkins and Mack Gromadzki
# Driver program for protocol

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
    for line in fileinput.input(files=name): # lines = numbers
        keyData += line
    e, d, N = keyData.split()
    user = RSA(name, int(e), int(d), int(N))
    return user

''' given a file of plaintext, return the encrypted blocks '''
def encryptFile(filename, target):
    plaintext = ""
    for line in fileinput.input(files=filename):
        plaintext += line
    ciphertext = target.encrypt(plaintext)
    #enc = open("enc.txt", "w") # if you want to write directly
    #enc.write(ciphertext)
    #enc.close()
    return ciphertext

''' given a file of encrypted blocks, return the plaintext '''
def decryptFile(filename, target):
    ciphertext = ""
    for line in fileinput.input(files=filename): # lines = blocks
        ciphertext += line
    plaintext = target.decrypt(ciphertext)
    return plaintext

''' input a file and return its signature '''
def signFile(filename, target):
    plaintext = ""
    for line in fileinput.input(files=filename):
        plaintext += str.rstrip(line)
    signature = target.sign(plaintext)
    return signature

''' given a file of encrypted blocks, return the plaintext '''
def checkFileSignature(filename, target):
    signature = ""
    for line in fileinput.input(files=filename): # lines = blocks
        signature += line
    plaintext = target.checkSignature(signature)
    return plaintext

''' driver function '''
def main(): # toy example
    target = sys.argv[2] + ".txt" # whose key to use
    target = getKeyPair(target)
    message = " ".join(sys.argv[3:])
    if sys.argv[1] == "encrypt":
        output = target.encrypt(message)
    elif sys.argv[1] == "decrypt":
        output = target.decrypt(message)
    elif sys.argv[1] == "sign":
        output = target.sign(message)
    elif sys.argv[1] == "checkSignature":
        output = target.checkSignature(message)
    elif sys.argv[1] == "encryptFile":
        output = encryptFile(sys.argv[3], target)
    elif sys.argv[1] == "decryptFile":
        output = decryptFile(sys.argv[3], target)
    elif sys.argv[1] == "checkFileSignature":
        output = checkFileSignature(sys.argv[3], target)
    elif sys.argv[1] == "signFile":
        output = signFile(sys.argv[3], target)
    print(output)

''' boilerplate '''
if __name__ == "__main__":
    main()

