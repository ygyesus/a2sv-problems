# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        num = start^goal

        bit = 0
        ans = 0
        while num>>bit:
            ans += num>>bit & 1
            bit += 1
        return ans