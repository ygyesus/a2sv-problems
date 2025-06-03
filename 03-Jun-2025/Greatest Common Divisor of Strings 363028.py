# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        divisors1 = []
        for end in range(len(str1)):
            string = str1[:end+1]
            if string*(len(str1)//len(string)) == str1:
                divisors1.append(string)

        divisors2 = []
        for end in range(len(str2)):
            string = str2[:end+1]
            print((end, string))
            if string*(len(str2)//len(string)) == str2:
                divisors2.append(string)

        maximum = ""

        print(divisors1)
        print(divisors2)
        for one in divisors1:
            for two in divisors2:
                if one==two and len(one) > len(maximum):
                    maximum = one

        return maximum
        
