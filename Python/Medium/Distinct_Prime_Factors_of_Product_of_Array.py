'''

    2521. Distinct Prime Factors of Product of Array

'''

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def countPrimes(n: int) -> int:
            if n <= 2:
                return [2]

            primes = [True for _ in range(n)]
            primes[0], primes[1] = False, False

            for i in range(2, n):
                if primes[i]:
                    for j in range(i * i, n, i):
                        primes[j] = False

            res = []
            for i, prime in enumerate(primes):
                if prime == True:
                    res.append(i)
            return res

        primes = countPrimes(max(nums) + 1)
        res = set()
        print(primes)
        for num in nums:
            for prime in primes:
                if num % prime == 0:
                    res.add(prime)
       
        return len(res)
