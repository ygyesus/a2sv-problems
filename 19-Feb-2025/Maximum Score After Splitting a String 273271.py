# Problem: Maximum Score After Splitting a String - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        leftSum = 0 if s[0] == '1' else 1

        rightSum = 0

        for i in range(1, len(s)):
            rightSum += int(s[i])

        score = maxScore = leftSum + rightSum

        for i in range(1, len(s)-1):
            if s[i] == '0':
                leftSum += 1

            elif s[i] == '1':
                rightSum -= 1


            score = leftSum + rightSum
            maxScore = max(maxScore, score)


        return maxScore