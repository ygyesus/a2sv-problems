# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo = {}
        def dfs(i):
            if not i in memo:
                maxAns = 0
                for j in range(i, n):
                    if nums[j] > nums[i]:
                        ans = dfs(j)
                        maxAns = max(maxAns, ans)
                memo[i] = maxAns+1

            return memo[i]

        maxAns = 0
        for i in range(n):
            ans = dfs(i)
            maxAns = max(maxAns, ans)

        return maxAns

        
