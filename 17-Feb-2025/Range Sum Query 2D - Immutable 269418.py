# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:


    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.prefix = [
            [0 for _ in range(self.cols)] for _ in range(self.rows)
        ]
        for i in range(self.rows):
            for j in range(self.cols):
                up = self.prefix[i-1][j] if i>0 else 0
                left = self.prefix[i][j-1] if j>0 else 0
                diag = self.prefix[i-1][j-1] if i>0 and j>0 else 0

                self.prefix[i][j] = up+left-diag + matrix[i][j]



        # print("MATRIX:")

        # for row in matrix:
        #     print(row)

        # print("================")        

        # print("PREFIX:")
        # for row in self.prefix:
        #     print(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        up = self.prefix[row1-1][col2] if row1>0 else 0
        left = self.prefix[row2][col1-1] if col1>0 else 0
        diag = self.prefix[row1-1][col1-1] if row1>0 and col1>0 else 0

        return self.prefix[row2][col2] - up - left + diag