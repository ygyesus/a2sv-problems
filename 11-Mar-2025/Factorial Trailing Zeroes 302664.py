# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:

        if n==0:
            return 0
        
        def factorial(n):
            if n==1 or n==0:
                return n

            return n*factorial(n-1)

        trailingZeroes = 0
        n = factorial(n)

        while n and n%10 == 0:
            n = n//10
            trailingZeroes += 1

        return trailingZeroes
        