# Problem: Reshape the Matrix - https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        rows, cols = len(mat), len(mat[0])

        if rows*cols != r*c: return mat

        newMat = [
            [0 for _ in range(c)] for _ in range(r)
        ]

        i = j = 0
        for row in range(rows):
            for col in range(cols):
                if j>=c:
                    i += 1
                    j = 0
                newMat[i][j] = mat[row][col]
                j += 1

        return newMat