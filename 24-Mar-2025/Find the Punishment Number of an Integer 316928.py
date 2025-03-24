# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def backtrack(string, currSum):
            
            if number < currSum:
                return False
            if string == '':
                if number == currSum:
                    return True

                return False
                
            for i in range(len(string)):
                num = int(string[:i+1])
                currSum += num
                
                if backtrack(string[i+1:], currSum):
                    return True

                currSum -= num

            return False
        
        total = 0
        for i in range(1, n+1):
            string = str(i**2)
            currSum = 0
            number = i
            if backtrack(string, currSum):
                total += i**2

        return total
