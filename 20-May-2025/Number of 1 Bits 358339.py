# Problem: Number of 1 Bits - https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ans = 0
        while n:
            ans += n&1
            n>>=1
        return ans