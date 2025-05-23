# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        '''
        num1 = 10111001
        '''

        setBits = 0
        right = 0

        # count setBits of num2
        while num2>>right:
            setBits += num2>>right & 1
            right += 1

        L, R = 0, num1
        maxBit = 0
        while L<=R:
            mid = (L+R)//2
            if 1<<mid >= num1:
                maxBit = mid
                R = mid-1
            else:
                L = mid+1
        x = 0
        while setBits and maxBit:
            if num1>>maxBit & 1:
                x += 1<<maxBit
                setBits -= 1

            maxBit -= 1

        bit = 0
        while setBits:
            if not x>>bit & 1:
                x += 1<<bit
                setBits -= 1
            bit += 1

        return x
