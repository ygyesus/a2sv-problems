# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        chars = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs",
        "tuv", "wxyz"]

        paths = []

        def backtrack(path, i):
            if i>=len(digits): 
                if path: paths.append(''.join(path))
                return

            digit = int(digits[i])
            for char in chars[digit]:
                path.append(char)
                backtrack(path, i+1)
                path.pop()

        backtrack([], 0)

        return paths

        
