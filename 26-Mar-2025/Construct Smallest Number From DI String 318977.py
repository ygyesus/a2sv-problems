# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        

        def backtrack(string, i, minString):

            if i>=len(pattern):
                return min(minString, string)

            
            num = int(string[-1])

            char = pattern[i]

            if char == 'I':
                for nextNum in range(num+1, 10):
                    if str(nextNum) in string:
                        continue
                    minString = min(minString, backtrack(string+str(nextNum), i+1, minString))

            elif char == 'D':
                for prevNum in range(1, num):
                    if str(prevNum) in string:
                        continue

                    minString = min(minString, backtrack(string+str(prevNum), i+1, minString))

            return minString

        string, i, minString = '', 0, '9'*(len(pattern)+1)

        ans = '9'*(len(pattern)+1)
        for num in range(1,10):
            ans = min(ans, backtrack(str(num), i, minString))
        
        return ans