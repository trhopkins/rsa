# Travis Hopkins and Mack Gromadski

from random import randint

class Prime:
    keysize = 32 # toy example, could be larger

    ''' boilerplate '''
    def __init__(self):
        pass

    ''' test for primes in sqrt(n)/6 time with 6k+-1 optimization '''
    def isPrime(self, n):
        if n == 2: # special case
            return True
        if n% 2 == 0 or n % 3 == 0:
            return False
        i = 5 # 6k-1
        while i ** 2 <= n:
            if n % i == 0 or n % (i+2) == 0:
                return False
            i += 6
        return True # https://en.wikipedia.org/wiki/Primality_test

    ''' find a prime within a range '''
    def genPrime(self, min=2, max=2**keysize):
        n = randint(min, max)
        while not self.isPrime(n):
            n = randint(min, max)
        return n

    ''' find primes p and q in range '''
    def genPrimes(self, min=2, max=2**keysize, count=2):
        primes = []
        while len(primes) < count:
            primes.append(self.genPrime(min, max))
        return primes

