# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        common = []

        t_index = 0

        for char in s:
            if t_index<len(t) and char == t[t_index]:
                common.append(char)
                t_index += 1

            if t_index >= len(t):
                break

        print(common)
        return len(t) - len(common)