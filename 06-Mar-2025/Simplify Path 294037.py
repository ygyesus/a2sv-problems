# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path = path.split("/")

        for char in path:
            if char == '.':
                pass
            elif char == '..':
                if stack:
                    stack.pop()

            elif char:
                stack.append(char)

        return "/" + "/".join(stack)
