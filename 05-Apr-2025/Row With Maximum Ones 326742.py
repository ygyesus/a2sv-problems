# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxIndex = maxSum = 0

        for i,row in enumerate(mat):
            if sum(row) > maxSum:
                maxIndex = i
                maxSum = sum(row)

        return [maxIndex, maxSum]