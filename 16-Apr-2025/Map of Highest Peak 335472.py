# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        rows = len(isWater)
        cols = len(isWater[0])

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        visited = set()

        q = deque()
        for row in range(rows):
            for col in range(cols):

                if isWater[row][col] == 1:
                    q.append((row, col))
                    visited.add((row, col))
                    isWater[row][col] = 0

        while q:
            for _ in range(len(q)):

                row,col = q.popleft()

                for row_d, col_d in directions:
                    new_row = row + row_d
                    new_col = col + col_d

                    if not (0<=new_row<rows and 0<=new_col<cols):
                        continue

                    if (new_row, new_col) in visited:
                        continue

                    isWater[new_row][new_col] = isWater[row][col] + 1
                    visited.add((new_row, new_col))
                    q.append((new_row, new_col))

        # for row in range(rows):
        #     for col in range(cols):
        #         isWater[row][col] -= 1

        return isWater




