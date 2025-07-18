# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        moves = 0
        prev = None

        while n>>moves:
            if (n>>moves & 1) == prev: return False
            prev = n>>moves & 1
            moves += 1

        return True