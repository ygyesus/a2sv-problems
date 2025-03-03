# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxIndex = 0

        for i in range(len(nums)):
            maxIndex = max(maxIndex, i+nums[i])

            if maxIndex >= len(nums)-1:
                return True

            if i==maxIndex and nums[i]==0:
                return False
        