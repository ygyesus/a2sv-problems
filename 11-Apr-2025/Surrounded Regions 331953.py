# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        height = len(board)
        width = len(board[0])

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        
        def isLegal(row,col):
            return 0<=row<height and 0<=col<width

        
        visited = set()
        
        def dfs(row, col):
            visited.add((row, col))
            for row_diff, col_diff in directions:
                new_row = row + row_diff
                new_col = col + col_diff

                if not isLegal(new_row, new_col):
                    continue

                if (new_row, new_col) in visited:
                    continue
                if board[new_row][new_col] == 'O':
                    dfs(new_row, new_col)

        # first row

        row = 0
        for col in range(width):
            if board[row][col] == 'X':
                continue

            # if (row,col) in visited:
            #     continue

            dfs(row, col)

        # last row
        
        row = height-1
        for col in range(width):
            if board[row][col] == 'X':
                continue
            # if (row, col) in visited:
            #     continue

            dfs(row, col)

        # first column

        col = 0
        for row in range(height):
            if board[row][col] == 'X':
                continue

            # if (row, col) in visited:
            #     continue

            dfs(row, col)

        # last column

        col = width-1
        for row in range(height):
            if board[row][col] == 'X':
                continue

            # if (row, col) in visited:
            #     continue

            dfs(row, col)

        for row in range(height):
            if row==0 or row==height-1:
                continue
            for col in range(width):
                if col==0 or col==width-1:
                    continue
                if (row,col) in visited:
                    continue
                    

                board[row][col] = 'X'

        print(visited)
                

        