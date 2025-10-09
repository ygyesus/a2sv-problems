# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        atMostGoal = atMostGoalMinusOne = 0

        left = 0
        total = 0
        # at most Goal
        for right in range(len(nums)):

            total += nums[right]

            while total > goal:
                if nums[left] == 1:
                    total -= 1
                left += 1

            atMostGoal += right-left+1

        # at most Goal minus one
        total=left=0
        for right in range(len(nums)):
            if goal-1<0:
                break
            total += nums[right]

            while total > goal-1:                
                if nums[left] == 1:
                    total -= 1
                left += 1

            atMostGoalMinusOne += right-left+1

        return atMostGoal - atMostGoalMinusOne
        

