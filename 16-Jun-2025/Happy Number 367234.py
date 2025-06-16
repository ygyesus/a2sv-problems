# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = {n}

        while n != 1:

            total = 0

            for num in str(n):
                total += int(num)**2

            if total in visited:
                return False
            visited.add(total)
            n = total

        return True