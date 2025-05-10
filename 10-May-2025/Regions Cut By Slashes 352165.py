# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class UnionFind:

    def __init__(self, n):
        
        self.root = {
            (row, col): (row, col) for col in range(n) for row in range(n)
        }

        self.rank = {
            (row, col): 0 for col in range(n) for row in range(n)
        }

    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty: return
        rankx, ranky = self.rank[rootx], self.rank[rooty]

        if rankx>ranky:
            self.root[rooty] = rootx
        elif ranky>rankx:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1



class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        def inbound(row, col): return 0<=row<n and 0<=col<n

        forwardSlash = '/'
        backSlash = '\\'
        space = ' '

        def func(char, row, col):
            row *= 3
            col *= 3
            if char == forwardSlash:

                newGrid[row+0][col+2] = char
                newGrid[row+1][col+1] = char
                newGrid[row+2][col+0] = char

            elif char == backSlash:

                newGrid[row+0][col+0] = char
                newGrid[row+1][col+1] = char
                newGrid[row+2][col+2] = char


        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

        newGridLength = n*3

        newGrid = [
            [space for _ in range(newGridLength)] for _ in range(newGridLength)
        ]

        for row in range(n):
            for col in range(n):
                char = grid[row][col]
                func(char, row, col)

        
        n*=3
        
        dsu = UnionFind(n)

        for row in range(n):
            for col in range(n):
                for row_d, col_d in neighbors:
                    new_row, new_col = row+row_d, col+col_d

                    if not inbound(new_row, new_col): continue

                    if newGrid[row][col] == newGrid[new_row][new_col] == space:
                        dsu.union((row, col), (new_row, new_col))


        SET = set()
        for row in range(n):
            for col in range(n):
                i,j = dsu.find((row, col))
                if newGrid[i][j] == space:
                    SET.add((i,j))

        return len(SET)
                    


            
        



        

        



        