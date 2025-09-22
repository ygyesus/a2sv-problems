# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1 for x in range(45+1)]
        memo[0], memo[1], memo[2] = 0, 1, 2

        def down(n):

            if not memo[n] != -1:
                memo[n] = down(n-1) + down(n-2)

            return memo[n]

        return down(n)