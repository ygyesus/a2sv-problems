# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        
        visited = set()
        stack = []
        for char in s:
            if char in visited:
                stack.append('.')
                visited = set()

            visited.add(char)


        stack = ''.join(stack)
        stack = stack.split('.')

        return len(stack)
