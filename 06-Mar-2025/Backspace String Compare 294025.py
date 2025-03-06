# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        def func(s, s_stack):
            for char in s:
                if char == '#':
                    if s_stack:
                        s_stack.pop()

                else:
                    s_stack.append(char)

            return s_stack

        return func(s, s_stack) == func(t, t_stack)