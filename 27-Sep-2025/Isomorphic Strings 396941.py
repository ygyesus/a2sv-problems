# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def helper(s, t):
            if len(s) != len(t): return False
            mapping = {}
            n = len(s)
            for i in range(n):
                if s[i] in mapping:
                    if mapping[s[i]] != t[i]: return False
                mapping[s[i]] = t[i]

            return True

        return helper(s, t) and helper(t, s)
