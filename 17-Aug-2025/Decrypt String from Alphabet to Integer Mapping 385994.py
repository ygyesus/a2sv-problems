# Problem: Decrypt String from Alphabet to Integer Mapping - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        start = ord('a')
        ans = []
        i = 0
        while i<len(s):
            order_delta = s[i]
            if i+2<len(s) and s[i+2] == '#':
                order_delta += s[i+1]

                i += 3
            else: i += 1

            order_delta = int(order_delta)
            char = chr(start+order_delta-1)
            ans.append(char)

        return ''.join(ans)