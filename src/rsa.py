#! /usr/bin/env python3

import prime

gen = prime.Prime()

def main():
    print("generating p and q...")
    print(gen.genPrimes())

if __name__ == "__main__":
    main()

