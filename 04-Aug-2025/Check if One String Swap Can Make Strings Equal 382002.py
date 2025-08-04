# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        for i in range(len(s1)):
            diff += s1[i] != s2[i]

            if diff>2: return False
        if diff==0: return True
        i = j = -1

        if diff not in (0,2): return False

        for index in range(len(s1)):
            if s1[index] != s2[index]:
                if i==-1: i = index
                else:
                    j = index
                    print(i,j)
                    if s1[i] == s2[j] and s2[i] == s1[j]:
                        return True
                    return False