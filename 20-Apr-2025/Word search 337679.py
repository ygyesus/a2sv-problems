# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # for row in board:
        #     print(row)

        # print("======================")
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        rows = len(board)
        cols = len(board[0])

        def inbound(row,col):
            return 0<=row<rows and 0<=col<cols

        def dfs(row,col,charIndex):
            visited.add((row, col))

            if charIndex+1 == len(word):
                return True

            for row_d, col_d in directions:
                # print(
                #     [board[duo[0]][duo[1]] for duo in visited]
                # )

                new_row = row + row_d
                new_col = col + col_d

                if (new_row, new_col) in visited:
                    continue

                if not inbound(new_row, new_col):
                    continue

                if not board[new_row][new_col] == word[charIndex+1]:
                    continue

                if dfs(new_row, new_col, charIndex+1):
                    return True
                else:
                    visited.remove((new_row, new_col))

            return False

        for row in range(rows):
            for col in range(cols):
                visited = set()
                visited.add((row, col))
                if not board[row][col] == word[0]:
                    continue

                if dfs(row, col, 0):
                    return True

        return False