# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        total = 0
        maxTotal = float('-inf')

        for i in range(k):
            total += nums[i]

        maxTotal = max(maxTotal, total)

        left = 0
        for right in range(k, len(nums)):
            total += nums[right] - nums[left]
            maxTotal = max(maxTotal, total)
            left += 1

        return maxTotal/k
        