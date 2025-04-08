# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        length = len(grid)
        def count(row,col):  
            if grid[row][col] == 0:
                return 0
            directions = [
                (0,1),
                (0, -1),
                (1,0),
                (-1,0)
            ]

            count = 0
            for x,y in directions:
                if not (0<=row+x<length and 0<=col+y<width) or grid[row+x][col+y] == 0:
                    count += 1

            return count

        ans = 0
        for row in range(length):
            for col in range(width):
                ans += count(row,col)

        return ans

