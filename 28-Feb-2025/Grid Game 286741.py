# Problem: Grid Game - https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        for i in range(1, len(grid[0])):
            grid[0][i] = grid[0][i-1]+grid[0][i]

        for i in range(1, len(grid[1])):
            grid[1][i] = grid[1][i-1]+grid[1][i]

        
        ans = float('inf')

# 1
# first suffix - grid[0][-1] - grid[0][i]
# second prefix - 

        for i in range(len(grid[0])):
            firstSuffixSum = grid[0][-1]-grid[0][i]
            secondPrefixSum = 0 if i==0 else grid[1][i-1]

            candidate = max(firstSuffixSum, secondPrefixSum)

            ans = min(ans, candidate)

        return ans

        