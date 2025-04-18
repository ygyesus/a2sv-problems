# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows = len(mat)
        cols = len(mat[0])

        visited = set()

        q = deque()

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        def inbound(row,col):
            return 0<=row<rows and 0<=col<cols

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    q.append((row, col))
                    visited.add((row,col))

        # Add to visited, THEN add to the queue (instantly)

        while q:
            # print(list(q))
            for _ in range(len(q)):
                (row,col) = q.popleft()
                

                for row_d, col_d in directions:
                    new_row = row + row_d
                    new_col = col + col_d

                    if (new_row, new_col) in visited or not inbound(new_row, new_col):
                        continue

                    mat[new_row][new_col] = mat[row][col] + 1
                    q.append((new_row, new_col))
                    visited.add((new_row, new_col))

        return mat

            






