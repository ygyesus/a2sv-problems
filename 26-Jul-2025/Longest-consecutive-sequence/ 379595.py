# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)<=1: return len(nums)
        nums.sort()
        count = 1
        maxCount = 1

        for i in range(1, len(nums)):

            if nums[i] == nums[i-1]: continue

            if nums[i] == nums[i-1]+1:
                count += 1
                maxCount = max(maxCount, count)
            else:
                maxCount = max(maxCount, count)
                count = 1

        return maxCount





