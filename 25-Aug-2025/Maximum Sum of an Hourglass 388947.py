# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0,0),
            (1, -1), (1, 0), (1, 1)
        ]
        def inbound(row, col): return 0<=row<rows and 0<=col<cols

        rows, cols = len(grid), len(grid[0])

        def getSum(row, col):
            total = 0
            for row_d, col_d in neighbors:
                new_row, new_col = row+row_d, col+col_d
                if not inbound(new_row, new_col): return 0
                total += grid[new_row][new_col]
            return total

        maxTotal = 0
        for row in range(rows):
            for col in range(cols):
                total = getSum(row, col)
                maxTotal = max(maxTotal, total)

        return maxTotal