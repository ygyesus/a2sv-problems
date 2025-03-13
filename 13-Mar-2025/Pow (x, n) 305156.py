# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n==0:
                return 1

            elif n<0:
                return 1/(power(x, abs(n)))
            else:
                if n%2 == 0:
                    y = power(x,n//2)
                    return y*y
                else:
                    return x*power(x, n-1)

        return power(x, n)