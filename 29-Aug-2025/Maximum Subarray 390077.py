# Problem: Maximum Subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxTotal = float('-inf')
        for i in range(len(nums)):
            total += nums[i]
            maxTotal = max(maxTotal, total)

            if total<0:
                total = 0

        return maxTotal