# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)

        values = list(counter.values())

        values.sort()

        flag = True
        # test against maximum of values

        k = values[-1]-1 or values[0]

        for i in range(len(values)-1):
            if values[i] != k:
                flag = False
                break
        if flag:
            return True

        flag = True
        # test agains minimum of values
        k = values[0] - 1 or values[1]

        for i in range(1, len(values)):
            if values[i] != k:
                return False

        return True


        