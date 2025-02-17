# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        array = [0] * len(s)

        for start, end, direction in shifts:
            if direction == 0:
                direction = -1

            array[start] += direction

            if end+1<len(s):
                array[end+1] -= direction

        # print(array)

        for i in range(1, len(array)):
            array[i] += array[i-1]

        # print(array)
        for i in range(len(s)):
            char = s[i]
            order = (ord(char) + array[i] - 97)%26 + 97
            s[i] = chr(order)

        return ''.join(s)