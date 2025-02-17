# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        ans = []

        for i in range(len(nums)):
            total += nums[i]
            ans.append(total)

        return ans