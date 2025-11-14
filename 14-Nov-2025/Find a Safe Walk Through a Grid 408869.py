# Problem: Find a Safe Walk Through a Grid - https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rows, cols = len(grid), len(grid[0])

        def inbound(row, col): return 0<=row<rows and 0<=col<cols

        if rows==cols==0: return True

        maxHealth = [
            [float('-inf') for _ in range(cols)] for _ in range(rows)
        ]
        maxHealth[0][0] = health-grid[0][0]

        heap = [(grid[0][0]-health, 0, 0)]

        heapify(heap)

        while heap:
            curr, row, col = heappop(heap)
            curr = -curr
            for row_d, col_d in directions:
                new_row, new_col = row+row_d, col+col_d
                if not inbound(new_row, new_col): continue
                new_health = curr-grid[new_row][new_col]
                if new_health>0 and new_row==rows-1 and new_col==cols-1: return True
                if not new_health>maxHealth[new_row][new_col]: continue
                maxHealth[new_row][new_col] = new_health
                heappush(heap, (-new_health, new_row, new_col))

        return False