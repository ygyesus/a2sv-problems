# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        bads = []
        strings = []
        def func(s):


            for i,char in enumerate(s):
                if not char.swapcase() in s:
                    func(s[:i])
                    func(s[i+1:])
                    return

            strings.append(s)

        func(s)
        # print(strings)

        longest = ""

        for string in strings:
            if len(string) > len(longest):
                longest = string

        return longest

            