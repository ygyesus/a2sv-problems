# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        def inbound(row, col): return 0<=row<rows and 0<=col<cols

        table = [
            [0 for _ in range(cols)] for _ in range(rows)
        ]

        table[0] = [member for member in matrix[0]]
        for row in range(1, rows):
            for col in range(cols):
                minAns = float('inf')
                for neighborCol in range(col-1, col+2):
                    if not inbound(row-1, neighborCol): continue
                    ans = matrix[row][col] + table[row-1][neighborCol]
                    minAns = min(minAns, ans)

                table[row][col] = minAns

        # for ROW in table: print(ROW)
        return min(table[-1])




        