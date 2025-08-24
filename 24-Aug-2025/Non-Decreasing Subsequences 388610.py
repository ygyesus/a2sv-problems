# Problem: Non-Decreasing Subsequences - https://leetcode.com/problems/non-decreasing-subsequences/description/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        paths = []
        def backtrack(i, path):
            if len(path) >= 2 and not path in paths:
                paths.append(path[:])
            for j in range(i+1, len(nums)):
                if path and not nums[j] >= path[-1]: continue
                path.append(nums[j])
                backtrack(j, path)
                path.pop()

        backtrack(-1, [])
        return paths
        

        