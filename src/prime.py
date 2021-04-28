from random import randint

class Prime:
    keysize = 32 # toy example, could be larger
    ''' boilerplate initialization code '''
    def __init__(self):
        pass

    ''' test for primes in sqrt(n)/3 time with 6k+-1 optimization '''
    def isPrime(self, n):
        if n == 2:
            return True
        if n% 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i ** 2 <= n:
            if n % i == 0 or n % (i+2) == 0:
                return False
            i += 6
        return True

    ''' find a prime in range '''
    def genPrime(self, min, max):
        found = False
        while not found:
            n = randint(min, max)
            if self.isPrime(n):
                return n

    ''' find primes p and q in range '''
    def genPrimes(self, min=2, max=2**keysize, count=2):
        primes = []
        while len(primes) < count:
            primes.append(self.genPrime(min, max))
        return primes

