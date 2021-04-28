from random import randint

class Prime:
    ''' boilerplate initialization code '''
    def __init__(self, keysize=256): # consider 32 for smaller numbers
        self.keysize = keysize

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

    ''' generate next prime given n '''
    def nextPrime(self, n):
        found = False
        while not found:
            n += 1
            if self.isPrime(n):
                found = True
        return n

    ''' generate next n primes given num, n '''
    def nextNPrimes(self, num, count):
        primes = []
        while len(primes) < count:
            num = self.nextPrime(num)
            primes.append(num)
        return primes

    ''' find a prime in range '''
    def genPrime(self, min, max):
        found = False
        while not found:
            n = randint(min, max)
            if self.isPrime(n):
                return n

    ''' find primes p and q in range '''
    def genPrimes(self, min, max, count=2):
        primes = []
        while len(primes) < count:
            primes.append(self.genPrime(min, max))
        return primes

