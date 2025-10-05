# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        
        memo = {}
        lengths = {len(word) for word in wordDict}

        def dfs(i):
            if i>=n: return True
            if not i in memo:
                for length in lengths:
                    if s[i:i+length] in wordDict and dfs(i+length):
                        memo[i] = True

            if not i in memo: memo[i] = False
            return memo[i]

        return dfs(0)

                    

