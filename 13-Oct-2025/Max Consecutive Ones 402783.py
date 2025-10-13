# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxCount = count = 0
        for num in nums:
            if num == 0: count = 0
            elif num == 1: count += 1

            maxCount = max(maxCount, count)

        return maxCount