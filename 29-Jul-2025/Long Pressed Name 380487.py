# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        freqOfName = []
        freqOfTyped = []

        curr = name[0]
        count = 0
        for i in range(len(name)):
            if name[i] == curr:
                count += 1
            else:
                freqOfName.append((curr, count))
                curr = name[i]
                count = 1

        freqOfName.append((curr, count))

        curr = typed[0]
        count = 0

        for i in range(len(typed)):
            if typed[i] == curr: count += 1
            else:
                freqOfTyped.append((curr, count))
                curr = typed[i]
                count = 1

        freqOfTyped.append((curr, count))

        # print(freqOfName)
        # print(freqOfTyped)

        if len(freqOfName) != len(freqOfTyped): return False

        for i in range(len(freqOfName)):
            charName, countName = freqOfName[i]
            charTyped, countTyped = freqOfTyped[i]
            if charName != charTyped: return False
            if countTyped<countName: return False

        return True