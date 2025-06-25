# Problem: Matrix Diagonal Sum - https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        total = 0
        n = len(mat)
        col = n-1
        
        for row in range(n):
            total += mat[row][row]
            if col != row:
                total += mat[row][col]

            col -= 1

        return total