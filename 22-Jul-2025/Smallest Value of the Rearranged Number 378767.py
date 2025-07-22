# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        
        def pos_func(positive):

            positive = list(str(positive))
            positive.sort()

            for i in range(len(positive)):
                if positive[i] != '0' and positive[0]=='0':
                    positive[i], positive[0] = positive[0], positive[i]
                    break

            return int(''.join(positive))

        def neg_func(negative):
            negative = list(str(negative)[1:])
            negative.sort(key = lambda x: -int(x))

            return int(''.join(negative)) * -1

        if num>=0: return pos_func(num)
        else: return neg_func(num)

        
