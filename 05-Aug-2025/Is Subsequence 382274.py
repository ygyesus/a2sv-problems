# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = j = 0

        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                if not i<len(s):
                    return True
            else:
                j += 1

        return not i<len(s)

        