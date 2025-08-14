# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        stack = []
        maxProduct = -1

        for factor in range(1, n):
            stack = []

            for times in range(n//factor):
                stack.append(factor)

            stack.append(n%factor)

            product = 1
            for num in stack: product *= num
            maxProduct = max(maxProduct, product)
            if len(stack)>=2:
                stack.append(stack.pop()+stack.pop())

            if len(stack)<2: continue
            product = 1
            for num in stack: product *= num
            maxProduct = max(maxProduct, product)

            

        return maxProduct