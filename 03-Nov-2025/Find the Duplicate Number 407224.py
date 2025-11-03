# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        state = 0

        for num in nums:
            if (state>>num) & 1: return num
            state = state | (1<<num)

        