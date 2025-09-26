# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        memo = {0: nums[0], 1: nums[1]}

        def dp(i):
            if not 0<=i: return 0
            if not i in memo:
                memo[i] = max(dp(i-2), dp(i-3)) + (nums[i] if i<len(nums) else 0)

            return memo[i]

        return max(dp(len(nums)-1), dp(len(nums)-2))