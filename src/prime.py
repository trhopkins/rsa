import random

class Prime:
    def __init__(self, keysize=256):
        self.keysize = keysize

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    '''
    test for prime numbers in O(sqrt(N)/3)) time with 6k+-1 optimization
    '''
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

