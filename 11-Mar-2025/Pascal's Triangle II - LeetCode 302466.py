# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def goOnce(row):
            ans = [1]

            for i in range(len(row)-1):
                ans.append(row[i] + row[i+1])

            ans.append(1)
            return ans

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1,1]

        row = [1,2,1]

        for _ in range(rowIndex - 2):
            row = goOnce(row)

        return row