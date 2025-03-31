# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def printMatrix(matrix):
            for row in matrix:
                print(row)

            # print("===============")
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


        ans = []
        def backtrack(rowIndex):
            if rowIndex == n:
                matrixCopy = deepcopy(matrix)
                for index in range(n):
                    row = matrixCopy[index]
                    matrixCopy[index] = ''.join(row)

                ans.append(matrixCopy)
                return

            for colIndex in range(n):
                matrix[rowIndex][colIndex] = 'Q'

                if not isValid(rowIndex, colIndex):
                    matrix[rowIndex][colIndex] = '.'
                    continue

                backtrack(rowIndex+1)
                matrix[rowIndex][colIndex] = '.'


        backtrack(0)
        

        # for matrix in ans:
        #     printMatrix(matrix)

        return ans
        

        