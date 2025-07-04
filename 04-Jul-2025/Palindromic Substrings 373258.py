# Problem: Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                count += s[i:j+1] == s[i:j+1][::-1]

        return count

        

        