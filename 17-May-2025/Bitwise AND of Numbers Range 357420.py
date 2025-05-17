# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        def isOne(left, right):
            if right-left > 0:
                # print(1)
                return False
            
            if not ((right&1) & (left&1)): 
                # print(left, right)
                # print(2)
                return False
            print(3)
            return True

        maximum = right.bit_length()
        ans = 0

        while maximum>=0:
            # print(left>>maximum, right>>maximum)
            # print("MAXIMUM:", maximum)
            if isOne(left>>maximum, right>>maximum):
                ans += 1<<maximum
            maximum -= 1

        return ans
