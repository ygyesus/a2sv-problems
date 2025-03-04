# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        papers = {5:0, 10:0, 20:0}
        for bill in bills:
            papers[bill] += 1
            change = bill - 5

            while change >= 20 and papers[20]:
                papers[20] -= 1
                change -= 20

            while change >= 10 and papers[10]:
                papers[10] -= 1
                change -= 10

            while change >= 5 and papers[5]:
                papers[5] -= 1
                change -= 5

            if change:
                return False

        return True