# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        popped = 0

        for i in range(len(s)):
            # print(stack, s[i])
            if s[i] == '(':
                stack.append(i)
            else:    
                j = stack.pop()
                
                if j+1==i:
                    score += 2**len(stack)
            # print(score)
            # print("==========")
        return score