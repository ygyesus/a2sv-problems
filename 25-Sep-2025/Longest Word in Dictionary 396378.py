# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        n = len(words)
        def check(i):

            for j in range(len(words[i])):
                if not words[i][:j+1] in words: return False
            return True

        ans = ''
        for i in range(n):
            if check(i):
                if len(ans) < len(words[i]):
                    ans = words[i]
                elif len(ans) == len(words[i]):
                    ans = min(ans, words[i])

        return ans