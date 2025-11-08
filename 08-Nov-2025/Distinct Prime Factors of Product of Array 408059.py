# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()
        for num in nums:    

            for factor in range(2, num+1):
                if num%factor == 0:
                    if not factor in factors:
                        factors.add(factor)
                    while num%factor == 0: num //= factor

        return len(factors)