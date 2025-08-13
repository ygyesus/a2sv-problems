# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:

        if not expression[0] in '+-':
            expression = '+' + expression

        stack = []
        left = 0
        for right in range(len(expression)):
            if expression[right] in '+-':
                stack.append(expression[left: right])
                left = right
        
        stack.append(expression[left:])
        print(stack)
        def compute(n1, d1, n2, d2):
            print((n1, d1))
            print((n2, d2))

            n = n1*d2 + n2*d1
            d = d1*d2

            GCD = gcd(n,d)
            n//=GCD
            d//=GCD

            return n,d

        n1 = 0
        d1 = 1

        for i in range(len(stack)):
            if not stack[i]:
                n2, d2 = 0, 1
            else:
                n2, d2 = stack[i][1:].split('/')
                n2, d2 = int(n2), int(d2)
                if stack[i][0] == '-': n2 *= -1

            n1, d1 = compute(n1, d1, n2, d2)
    
        return str(n1)+'/'+str(d1)




            


