# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = {}
        memo[0] = 0
        memo[1] = memo[2] = 1

        def dp(a):
            if not a in memo:
                memo[a] = dp(a-3) + dp(a-2) + dp(a-1)

            return memo[a]

        return dp(n)

