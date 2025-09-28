# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}
        def dfs(i):
            if i>=len(cost)-2: return cost[i]
            if not i in memo:
                additional = min(dfs(i+1), dfs(i+2))
                memo[i] = additional + cost[i]
            return memo[i]

        return min(dfs(0), dfs(1))
        

