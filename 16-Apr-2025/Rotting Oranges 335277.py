# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        rotten = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten.append((row, col))





        visited = set(rotten)
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        zeroes = 0

        count = 0
        while rotten:
            levelLength = len(rotten)
            haveNewRotten = False
            while levelLength:
                row, col = rotten.popleft()

                # print("considering", (row, col), "....")
                # for ROW in grid:
                #     print(ROW)

                # print("===============")

                for row_d, col_d in directions:
                    new_row = row + row_d
                    new_col = col + col_d

                    if not (0<=new_row<rows and 0<=new_col<cols):
                        continue

                    if grid[new_row][new_col] == 2:
                        continue

                    if grid[new_row][new_col] == 0:
                        # zeroes += 1
                        continue

                    haveNewRotten = True
                    rotten.append((new_row, new_col))
                    grid[new_row][new_col] = 2
                    
                levelLength -= 1

            if not haveNewRotten:
                break
            else:
                count += 1

        # for row in grid:
        #     print(row)
        for row in grid:
            if row.count(1):
                return -1

        return count

        

            

                    
                





