# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows, cols = len(matrix), len(matrix[0])
        ROWS = set()
        COLS = set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    ROWS.add(row)
                    COLS.add(col)

        for row in ROWS:
            for col in range(cols):
                matrix[row][col] = 0

        for col in COLS:
            for row in range(rows):
                matrix[row][col] = 0

        