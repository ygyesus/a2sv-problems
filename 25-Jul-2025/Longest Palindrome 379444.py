# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        values = list(counter.values())

        evenCount = 0
        oddExists = False
        for i, value in enumerate(values):
            if value%2==0:
                evenCount += value
            else:
                evenCount += value-1
                oddExists = True

        if oddExists:
            return evenCount + 1
        else: return evenCount

