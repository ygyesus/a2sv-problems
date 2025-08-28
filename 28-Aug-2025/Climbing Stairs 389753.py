# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = dict()

        def dp(i):
            if not i in memo:
                memo[i] = dp(i-1) + dp(i-2)

            return memo[i]

        memo[1] = 1
        memo[2] = 2

        return dp(n)