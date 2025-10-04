# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                matrix[row][col] = int(matrix[row][col])

        for ROW in matrix: print(ROW)
        # print("===============")
        for row in range(rows-2, -1, -1):
            for col in range(cols-2, -1, -1):
                diag = matrix[row+1][col+1]
                right = matrix[row][col+1]
                down = matrix[row+1][col]
                if min(diag, right, down) > 0 and matrix[row][col]: 
                    # print((row, col))
                    matrix[row][col] = min(diag, right, down) + matrix[row][col]

        maxAns = 0
        for row in range(rows):
            for col in range(cols):
                ans = matrix[row][col]
                maxAns = max(maxAns, ans)

        # for ROW in matrix: print(ROW)

        return maxAns**2