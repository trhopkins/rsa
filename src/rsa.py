#! /usr/bin/env python3

import prime

gen = prime.Prime()

def main():
    print("find the next prime after 2^32:", gen.nextPrime(2**32))
    print("find the next 5 primes after 1,000,000:", gen.nextNPrimes(1000000, 5))
    print("find a prime with a keysize of 10:", gen.genPrime(2, 2**10))
    print("generating prime numbers between 1 and 1,000...")
    print(gen.genPrimes(2, 1000, 10))

if __name__ == "__main__":
    main()

