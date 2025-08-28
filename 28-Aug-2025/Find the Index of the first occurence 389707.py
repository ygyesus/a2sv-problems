# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            if haystack[i: i+len(needle)] == needle: return i
        return -1