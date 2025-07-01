# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
        if len(s)==1: return 1
        count = 0

        left = 0
        maxLength = float('-inf')
        
        for right in range(1, len(s)):
            count += s[right-1]==s[right]

            while count>1:
                count -= s[left]==s[left+1]
                left += 1

            maxLength = max(maxLength, right-left+1)

        return maxLength

            