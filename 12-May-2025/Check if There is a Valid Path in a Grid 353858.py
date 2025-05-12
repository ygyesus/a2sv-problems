# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class UnionFind:
    def __init__(self, rows, cols):
        self.rank = {(row, col): 0 for row in range(rows) for col in range(cols)}
        self.root = {(row, col): (row, col) for row in range(rows) for col in range(cols)}

    def find(self, x):
        if x==self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def getCoords(num):
        for row in range(rows):
            for col in range(cols):
                if num==0: return (row, col)
                num -= 1

    def union(self, x,y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            elif self.rank[rootx]> self.rank[rooty]:
                self.root[rooty] = rootx
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        rows = len(grid)
        cols = len(grid[0])
        product = rows*cols
        dsu = UnionFind(rows, cols)

        def inbound(row,col):
            return 0<=row<rows and 0<=col<cols

        def check(row1, col1, row2, col2):
            # assumes row1==row2 and col2 == co1+1 or row2 == row+1 and col1==col2
            if not inbound(row1, col1): return False
            if not inbound(row2, col2): return False

            if (col2-col1 == 1):
                if grid[row1][col1] in (1, 4, 6) and grid[row2][col2] in (1, 3, 5):
                    return True
                return False

            if (row2-row1 == 1):
                if grid[row1][col1] in (2, 3, 4) and grid[row2][col2] in (2, 5, 6):
                    return True
                return False

        neighbors = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        for row1 in range(rows):
            for col1 in range(cols):
                for row_d, col_d in neighbors:
                    row2 = row1+row_d
                    col2 = col1+col_d


                    if check(row1, col1, row1, col2):
                        dsu.union((row1, col1), (row1, col2))

                    if check(row1, col1, row2, col2):
                        dsu.union((row1, col1), (row2, col1))

        if dsu.find((0,0)) == dsu.find((rows-1, cols-1)):
            return True

        return False




