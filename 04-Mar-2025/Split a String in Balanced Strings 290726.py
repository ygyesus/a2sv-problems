# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = 0
        l = r = 0
        for char in s:
            if char == 'L':
                l += 1
            elif char == 'R':
                r += 1

            if l==r:
                total += 1

        return total
