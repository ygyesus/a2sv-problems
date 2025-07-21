# Problem: Remove K Digits - https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k and (stack and stack[-1]>digit):
                stack.pop()
                k -= 1

            stack.append(digit)

        print(stack)
        while k:
            stack.pop()
            k -= 1

        print(stack)
        
        
        stack = stack[::-1]
        while stack and stack[-1] == '0':
            stack.pop()

        print(stack)
        stack = stack[::-1]
        x = ''.join(stack)
        if not stack: return '0'
        return x