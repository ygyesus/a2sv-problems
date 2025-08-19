# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        SET = set(nums)
        visited = set()

        maxCount = float('-inf')

        nums = nums[::-1]

        for num in nums:
            if num in visited: continue
            visited.add(num)
            count = 1
            while True:
                num = num**0.5
                if num in visited: break
                if not num in SET: break
                visited.add(num)
                count += 1

            maxCount = max(maxCount, count)

        if maxCount == 1: return -1
        return maxCount

