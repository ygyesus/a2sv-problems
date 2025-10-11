# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []

        for char in s:

            stack.append(char)
            if len(stack) >= k and stack[-k:] == [char] * k:
                for _ in range(k): stack.pop()

        return ''.join(stack)

            

