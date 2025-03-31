# Problem: N-Queens II - https://leetcode.com/problems/n-queens-ii/description/

class Solution:
    def totalNQueens(self, n: int) -> int:

        matrix = [
            ['.' for _ in range(n)] for _ in range(n)
        ]

        def isValid(i,j):
            queens = 0
            for row in range(n):
                for col in range(n):
                    if row==i or col==j or row+col==i+j or row-col==i-j:
                        if matrix[row][col] == 'Q':
                            queens += 1
                            if queens > 1:
                                return False

            return True


        ans = [0]
        def backtrack(rowIndex):
            if rowIndex == n:
                ans[0] += 1
                return

            for colIndex in range(n):
                matrix[rowIndex][colIndex] = 'Q'

                if not isValid(rowIndex, colIndex):
                    matrix[rowIndex][colIndex] = '.'
                    continue

                backtrack(rowIndex+1)
                matrix[rowIndex][colIndex] = '.'


        backtrack(0)

        return ans[0]