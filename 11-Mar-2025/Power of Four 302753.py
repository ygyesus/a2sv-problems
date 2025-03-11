# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return False

        def func(n):
            if n%4 == 0:
                return func(n//4)

            return n==1

        return func(n)