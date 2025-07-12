# Problem: Ugly Number - https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        
        def func(num):

            if num==0: return False

            while num%2==0: num//=2
            while num%3==0: num//=3
            while num%5==0: num//=5

            return num == 1

        return func(n)


            

