# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        def inbound(row, col):
            return 0<=row<rows and 0<=col<cols

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        original = image[sr][sc]

        q = deque([(sr,sc)])
        visited = set()

        while q:

            for _ in range(len(q)):
                row, col = q.popleft()
                image[row][col] = color

                visited.add((row, col))

                for row_d, col_d in directions:
                    new_row = row+row_d
                    new_col = col+col_d

                    if (new_row, new_col) in visited:
                        continue

                    if not inbound(new_row, new_col):
                        continue

                    if image[new_row][new_col] != original:
                        continue


                    
                    image[new_row][new_col] = color
                    q.append((new_row, new_col))


        return image



        