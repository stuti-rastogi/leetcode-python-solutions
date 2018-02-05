class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if (n <= 2):
        #     return 0
        # primes = [True for i in range(n)]
        # for i in range(2,len(primes)):
        #     if (primes[i]):
        #         for j in range(i**2, n, i):
        #             primes[j] = False
        # count = -2
        # for p in primes:
        #     if (p):
        #         count = count + 1
        # return count
    
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)