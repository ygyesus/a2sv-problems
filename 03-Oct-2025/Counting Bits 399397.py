# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        memo = [-1 for _ in range(n+1)]
        if 0<len(memo): memo[0] = 0
        if 1<len(memo): memo[1] = 1

        def dp(i):
            if memo[i] == -1:
                memo[i] = dp(i//2) + (i&1)

            return memo[i]

        for i in range(n+1): memo[i] = dp(i)
        return memo