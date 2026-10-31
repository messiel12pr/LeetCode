'''

    204. Count Primes

'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        primes = [True for _ in range(n)]
        primes[0], primes[1] = False, False

        for i in range(2, n):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False

        res = 0
        for i, prime in enumerate(primes):
            if prime == True:
                res += 1
        return res
