# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:

        if n==1:
            return False
        if int(n**0.5)==n**0.5:
            for num in range(2,int(n**0.5)):
                if n%num==0:
                    return False
            return True
        
        return False