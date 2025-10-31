# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        SUM_OF_XOR_TOTALS = 0

        for mask in range(1<<n):
            XOR_TOTAL = 0
            i = 0
            while mask>>i:
                if (mask>>i) & 1: XOR_TOTAL ^= (nums[i])
                i += 1
            SUM_OF_XOR_TOTALS += XOR_TOTAL

        return SUM_OF_XOR_TOTALS
            



