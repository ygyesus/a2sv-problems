# Problem: E - Kidus and Robot - https://codeforces.com/gym/604781/problem/E

import threading
import sys
from math import floor, ceil, sqrt
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right

input = lambda: sys.stdin.readline().strip()

def getArray(): return list(map(int, input().split()))

def getIndices(base): return list(map(lambda x: int(x) - base, input().strip().split()))
# Use getIndices(0) or getIndices(1) as needed

INT = lambda: int(input().strip())
LIST = lambda: input().strip().split()
INTS = lambda: list(map(int, LIST()))
MATRIX = lambda rows, cols: [INTS() for _ in range(rows)]
# MATRIX(rows,cols)

#############################################################################





def solve():
    rows,cols,k = INTS()


    grid = []
    occupied = '*'
    robot = 'X'
    empty = '.'
    for _ in range(rows):
        row = list(input())
        # occupied, robot, empty

        grid.append(row)

    if k%2:
        print("IMPOSSIBLE")
        return

    robotRow, robotCol = None, None
    found = False
    for row in range(rows):
        if found:
            break
        for col in range(cols):
            if grid[row][col] == robot:
                robotRow, robotCol = row, col
                found = True
                break

    # for member in grid:
    #     print(member)
    
    directions = {
        'D': (1,0),
        'L': (0,-1),
        'R': (0,1),
        'U': (-1,0)
    }

    opposite = {
        'D': 'U',
        'U': 'D',
        'L': 'R',
        'R': 'L'
    }



    def inbound(row, col):
        return 0<=row<rows and 0<=col<cols


    shortest_path = [
        [None for _ in range(cols)] for _ in range(rows)
    ]

    

    row, col = robotRow, robotCol
    found = False
    
    for char in directions:
        row_d, col_d = directions[char]
        new_row, new_col = row + row_d, col + col_d
        if not inbound(new_row, new_col): continue

        if grid[new_row][new_col] == empty:
            found = True
            break
    
    if not found: 
        print("IMPOSSIBLE")
        return


    # BFS

    q = deque([(row, col)])
    # print(shortest_path)
    shortest_path[row][col] = 0

    distance = 0
    while q:
        row, col = q.popleft()
        # if not shortest_path[new_row][new_col] == None: continue
        for char in directions:
            row_d, col_d = directions[char]
            new_row, new_col = row + row_d, col + col_d
            # print("NEWS:", new_row, new_col)
            if not inbound(new_row, new_col): continue
            if not grid[new_row][new_col] == empty: continue
            if not shortest_path[new_row][new_col] == None: continue
            shortest_path[new_row][new_col] = shortest_path[row][col] + 1
            q.append((new_row, new_col))




    # print(shortest_path)

    ans = []
    row, col = robotRow, robotCol
    for i in range(k):
        j = i+1
        for char in directions:
            row_d, col_d = directions[char]
            new_row, new_col = row + row_d, col + col_d

            if not inbound(new_row, new_col): continue
            # print(new_row, new_col)
            if grid[new_row][new_col] == occupied: continue
            if shortest_path[new_row][new_col] == None: continue

            forward = i+1
            backward = shortest_path[new_row][new_col]


            if not forward+backward <= k: continue
            row, col = new_row, new_col
            ans.append(char)
            break

    print(''.join(ans))
            












                
        

        





def main():
    t = 1
    # t = int(input())
    for _ in range(t):
        solve()






#############################################################################





if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()