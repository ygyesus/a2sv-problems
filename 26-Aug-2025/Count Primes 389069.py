# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True for _ in range(n+1)]
        if len(is_prime) >= 1: is_prime[0] = True
        if len(is_prime) >= 2: is_prime[1] = True

        i = 2

        while i*i<=n:
            if len(is_prime) >= i+1:
                is_prime[i]
                j = i*i

                while j<=n:
                    is_prime[j] = False
                    j += i

            i += 1

        count = 0
        for i in range(2, n+1):
            count += (i<n and is_prime[i])

        return count
