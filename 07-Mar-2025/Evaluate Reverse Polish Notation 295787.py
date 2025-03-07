# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if not token in operators:
                stack.append(token)

            else:
                y = int(stack.pop())
                x = int(stack.pop())
                print(x, token, y)

                if token == '+':
                    result = x+y

                elif token == '-':
                    result = x-y

                elif token == '*':
                    result = x*y
                
                elif token == '/':
                    if x/y < 0:
                        result = ((-1*x)//y) * (-1)
                    else:
                        result = x//y

                stack.append(result)

        return int(stack.pop())