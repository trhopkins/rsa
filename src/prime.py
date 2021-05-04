# prime generator
# Travis Hopkins and Mack Gromadzki

from random import randint

class Prime:
    keysize = 64 / 2 # used to generate p and q which are multiplied

    ''' boilerplate '''
    def __init__(self):
        pass # only here for posterity

    ''' test for primes in sqrt(n)/6 time with 6k+-1 optimization '''
    def isPrime(self, n): # 100% certainty of prime/not prime
        if n == 2: # special case
            return True
        if n% 2 == 0 or n % 3 == 0:
            return False
        k = 5 # 6k-1
        while k ** 2 <= n:
            if n % k == 0 or n % (k+2) == 0:
                return False
            k += 6
        return True # https://en.wikipedia.org/wiki/Primality_test

    ''' faster prime test, O(log(N)) complexity '''
    def rabinMiller(self, n, d): # nondeterministic, try multiple times
        tmp = randint(2, (a - 4))
        x = pow(tmp, d, n) # faster than expMod but identical
        #x = expMod(tmp, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1: # Fermat's little theorem, SICP page 52
            x = pow(x, 2, n)
            d *= 2
            if x == 1:
                return False
            elif x == n - 1: # think of a clearer way to write this?
                return True
        return False # not prime

    ''' find a prime within a range '''
    def genPrime(self, min=2**(keysize-1), max=2**keysize-1):
        n = randint(min, max)
        while not self.isPrime(n):
            n = randint(min, max) # guess and check
        return n

    ''' find primes p and q in range '''
    def genPrimes(self, min=2**(keysize-1), max=2**keysize-1, count=2):
        primes = []
        while len(primes) < count:
            primes.append(self.genPrime(min, max))
        return primes

    ''' modular exponent function. Still slower than builtin pow '''
    def expMod(self, b, e, m): # base^exponent mod modulus
        if e == 1:
            return b % m
        x = self.expMod(b, e>>1, m)
        x = (x * x) % m
        if e & 1 == 1: # if odd shortcut
            x = (x * b) % m
        return x # see SICP page 56

