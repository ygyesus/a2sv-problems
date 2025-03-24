# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:

        ans = []
        binary = []
        def backtrack(binary, n):
            if len(binary) == n:
                ans.append(''.join(binary))
                return
            

            for char in '01':
                if binary and binary[-1] == char == '0':
                    continue
                binary.append(char)
                backtrack(binary, n)
                binary.pop()

        backtrack(binary, n)
        return ans