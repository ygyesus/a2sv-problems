# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counterS = Counter(s)
        counterT = Counter(t)

        for char in counterT:
            if counterS[char] + 1 == counterT[char]: return char
    
        # return False