# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        height = len(grid)
        width = len(grid[0])

        def inbound(duo):
            i,j = duo
            return 0<=i<height and 0<=j<width

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]


        def dfs(row, col):
            visited.add((row, col))
            newArea = grid[row][col]
            

            for row_dir, col_dir in directions:
                new_row = row + row_dir
                new_col = col + col_dir

                if not inbound((new_row, new_col)):
                    continue

                if (new_row, new_col) in visited:
                    continue

                if grid[new_row][new_col] == 0:
                    continue

                newArea += dfs(new_row, new_col)

            return newArea

        maxArea = 0

        for row in range(height):
            for col in range(width):
                if grid[row][col] == 0:
                    continue
                area = dfs(row, col)
                maxArea = max(maxArea, area)

        return maxArea



            

                

                

