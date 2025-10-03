# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:

        def isValid(substring):
            return substring[0] != '0' and 1<=int(substring)<=26
        # if '0' in s or s=='': return 0

        n = len(s)
        dp = [0 for _ in range(n)]
        dp[0] += isValid(s[0])
        if 1<n: 
            dp[1] += dp[0] and isValid(s[1])
            dp[1] += isValid(s[:2])

        for i in range(2, n):
            
            if isValid(s[i-1:i+1]): dp[i] += dp[i-2]
            if isValid(s[i]): dp[i] += dp[i-1]
        print(dp)
        return dp[n-1]





