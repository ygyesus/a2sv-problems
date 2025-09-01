# Problem: Count Servers that Communicate - https://leetcode.com/problems/count-servers-that-communicate/description/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(currRow, currCol):
            # print((currRow, currCol))
            visited.add((currRow, currCol))
            count = 0

            for row in range(rows):
                if (row, currCol) in visited: continue
                if grid[row][currCol] == 0: continue
                childCount = dfs(row, currCol)
                if childCount == 0: count += 1
                else: count += childCount

            for col in range(cols):
                if (currRow, col) in visited: continue
                if grid[currRow][col] == 0: continue
                childCount = dfs(currRow, col)
                if childCount == 0: count += 1
                else: count += childCount

            if count>0: count += 1
            return count

        count = 0
        for currRow in range(rows):
            for currCol in range(cols):  
                if (currRow, currCol) in visited: continue
                if grid[currRow][currCol] == 0: continue
                count += dfs(currRow, currCol)
                
        return count


