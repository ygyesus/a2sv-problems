# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n

        def inbound(row, col): return 0<=row<rows and 0<=col<cols

        grid = [
            [0 for _ in range(cols)] for _ in range(rows)
        ]

        for col in range(cols):
            grid[0][col] = 1

        for row in range(rows):
            grid[row][0] = 1

        if rows>=2: grid[1][0] = 1

        for row in range(1, rows):
            for col in range(1, cols):
                topRow, topCol = row-1, col
                leftRow, leftCol = row, col-1
                if inbound(topRow, topCol): grid[row][col] += grid[topRow][topCol]
                if inbound(leftRow, leftCol): grid[row][col] += grid[leftRow][leftCol]

        # for ROW in grid: print(ROW)
        return grid[-1][-1]



