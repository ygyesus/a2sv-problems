# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        visited = set()

        rows, cols = len(matrix), len(matrix[0])

        # down
        for row in range(rows):
            col = 0
            val = matrix[row][col]

            while row<rows and col<cols:
                if matrix[row][col] != val: return False
                row += 1
                col += 1

        # right

        for col in range(1, cols):
            row = 0
            val = matrix[row][col]

            while row<rows and col<cols:
                if matrix[row][col] != val: return False
                row += 1
                col += 1

        return True
