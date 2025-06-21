# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        

        ans = 0

        while k and numOnes:
            ans += 1

            numOnes -= 1
            k -= 1

        while k and numZeros:
            ans += 0

            numZeros -= 1
            k -= 1

        while k and numNegOnes:
            ans += -1

            numNegOnes -= 1
            k -= 1

        return ans