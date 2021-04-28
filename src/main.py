#! /usr/bin/env python3

# Travis Hopkins and Mack Gromadski

import rsa

keyGen = rsa.RSA()

''' driver function '''
def main(): # toy example, no key generation yet
    p, q = keyGen.genPQ()
    e, d, N = keyGen.genKeyPair(p, q); # ed = 1 mod phiN, see page 96
    #p = 11; q = 17; N = p * q; phiN = (p - 1) * (q - 1); e = 13; d = keyGen.multInv(e, phiN)
    msg = "Hello, world"
    ciphertext = keyGen.encrypt(e, N, msg)
    plaintext = keyGen.decrypt(d, N, ciphertext)
    print(ciphertext)
    print(plaintext)

''' boilerplate '''
if __name__ == "__main__":
    main()

