# Problem: Unique Paths III - https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        start, end, empty, obstacle = 1,2,0,-1
        paths = []

        rows, cols = len(grid), len(grid[0])

        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]

        empties = 0
        for row in range(rows):
            for col in range(cols):
                empties += grid[row][col]==empty

        def inbound(row, col): return 0<=row<rows and 0<=col<cols

        def backtrack(path, duo):
            row, col = duo
            # (row, col) is already added
            if grid[row][col] == end:
                if len(path)==empties+2:
                    paths.append(path[:])

                return

            for row_d, col_d in directions:
                new_row, new_col = row+row_d, col+col_d
                if not inbound(new_row, new_col): continue
                if (new_row, new_col) in path: continue
                if grid[new_row][new_col] == obstacle: continue

                path.append((new_row, new_col))
                backtrack(path, (new_row, new_col))
                path.pop()

        found = False
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == start: 
                    found = True
                    break

            if found: break
        
        backtrack([(row, col)], (row, col))

        for path in paths: print(path)

        return len(paths)