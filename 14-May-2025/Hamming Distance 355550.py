# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x^y

        count = 0
        while res:
            count += res & 1
            res >>= 1

        return count