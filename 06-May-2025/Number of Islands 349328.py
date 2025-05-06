# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class UnionFind:

    def __init__(self, nodes):
        self.root = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, x):

        if x!=self.root[x]:
            return self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty: return

        rankx = self.rank[rootx]
        ranky = self.rank[rooty]

        if rankx > ranky:
            self.root[rooty] = rootx
        elif ranky > rankx:
            self.root[rootx] = rooty
        elif rankx == ranky:
            self.root[rooty] = rootx
            self.rank[rootx] += 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        inbound = lambda row,col: 0<=row<rows and 0<=col<cols

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        
        nodes = []
        
        for row in range(rows):
            for col in range(cols):
                if not grid[row][col] == '1': continue
                node = (row, col)
                nodes.append(node)

        dsu = UnionFind(nodes)


        for row, col in nodes:
            dsu.find((row, col))
            node = (row, col)
            for row_d, col_d in directions:
                new_row, new_col = row+row_d, col+col_d
                if inbound(new_row, new_col) and grid[new_row][new_col] == '1':
                
                    neighbor = (new_row, new_col)

                    dsu.union(node, neighbor)

        roots = [dsu.find(node) for node in nodes]
        return len(set(roots))

