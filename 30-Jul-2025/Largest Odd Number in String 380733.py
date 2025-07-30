# Problem: Largest Odd Number in String - https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        lastOddIndex = None
        for i in range(len(num)):
            if int(num[i])%2==1:
                lastOddIndex = i

            # print(lastOddIndex)

        if lastOddIndex==None: return ""

        return num[0:lastOddIndex+1]