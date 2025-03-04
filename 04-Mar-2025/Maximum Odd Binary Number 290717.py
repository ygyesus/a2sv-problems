# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = sorted(s)

        if s[0] != '1':
            print("HERE")
            for i in range(len(s)):
                if s[i] == '1':
                    s[0], s[i] = s[i], s[0]
                    print(s)
                    break

        # print(s)
        return ''.join(s[::-1])

