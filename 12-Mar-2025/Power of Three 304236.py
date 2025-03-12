# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def powerOfThree(n):
            if n%3:
                return n==1

            if n==0:
                return False

            return powerOfThree(n//3)

        return powerOfThree(n)
