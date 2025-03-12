# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def powerOfTwo(n):

            if n%2 == 1:
                return n==1
            if n==0:
                return False
            return powerOfTwo(n//2)

        return powerOfTwo(n)