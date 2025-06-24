# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        rows, cols = m, n

        if len(original) != rows*cols:
            return []

        i = 0
        matrix = []
        for row in range(rows):
            ROW = []
            for col in range(cols):
                ROW.append(original[i])
                i += 1

            matrix.append(ROW)

        return matrix