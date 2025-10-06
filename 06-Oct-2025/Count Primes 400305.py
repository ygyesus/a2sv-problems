# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True for _ in range(n)]

        if 0<n: isPrime[0] = False
        if 1<n: isPrime[1] = False

        for prime in range(n):
            if isPrime[prime]:
                for multiple in range(2*prime, n, prime):
                    isPrime[multiple] = False

        return isPrime.count(True)