# Problem: Number of Ways to Select Buildings - https://leetcode.com/problems/number-of-ways-to-select-buildings/

class Solution:
    def numberOfWays(self, s: str) -> int:
        # 010
        # 101

        freq = Counter(s)
        zeroes = freq['0']
        ones = freq['1']

        # 010

        zeroesEncountered = onesEncountered = 0

        ways = 0
        for char in s:
            if char == '1':
                ways += zeroesEncountered * (zeroes-zeroesEncountered)
            else:
                zeroesEncountered += 1

        for char in s:
            if char == '0':
                ways += onesEncountered * (ones-onesEncountered)
            else:
                onesEncountered += 1

        return ways

        




        