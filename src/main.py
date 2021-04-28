#! /usr/bin/env python3

import rsa

# Travis Hopkins and Mack Gromadski

''' driver function '''
def main(): # toy example, no key generation yet
    keyGen = rsa.RSA()
    p = 11
    q = 17
    N = p * q
    phiN = (p - 1) * (q - 1)
    e = 13
    d = keyGen.multInv(e, phiN)
    # ed = 1 mod phiN, see book page 96
    msg = "Hello, world"
    ciphertext = keyGen.encrypt(e, N, msg)
    plaintext = keyGen.decrypt(d, N, ciphertext)
    print(ciphertext)
    print(plaintext)

''' boilerplate call to driver method '''
if __name__ == "__main__":
    main()

