# Problem: Validate Stack Sequences - https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        push = pop = 0

        while push<len(pushed) and pop<len(popped):
            if stack and stack[-1] == popped[pop]:
                stack.pop()
                pop += 1
            else:
                stack.append(pushed[push])
                push += 1

        while push<len(pushed):
            stack.append(push)
            push += 1

        while pop<len(popped) and stack and stack[-1] == popped[pop]:
            stack.pop()
            pop += 1

        return stack == []
            

        