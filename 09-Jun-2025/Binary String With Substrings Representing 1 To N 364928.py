# Problem: Binary String With Substrings Representing 1 To N - https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        
        for num in range(1, n+1):
            if not (bin(num)[2:]) in s:
                return False

        return True