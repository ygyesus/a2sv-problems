# Problem: B - Mihret and Chess - https://codeforces.com/gym/604781/problem/B

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
    row1, col1, row2, col2 = INTS()

    def king(row1, row2, col1, col2):
        moves = 0
        
        while True:
            if row1 == row2 and col1 == col2:
                break
            if row1 < row2:
                row1 += 1
            elif row1 > row2:
                row1 -= 1

            if col1 < col2:
                col1 += 1

            elif col1 > col2:
                col1 -= 1
            moves += 1

        return moves
    
    def rook(row1, row2, col1, col2):
        moves = 0

        while True:
            if row1 == row2 and col1 == col2:
                break

            if row1 != row2:
                row1 = row2
                
            elif col1 != col2:
                col1 = col2

            moves += 1

        return moves
    
    def bishop(row1, row2, col1, col2):
        if not((row1+col1)%2 == (row2+col2)%2):
            return 0
        
        if row1==row2 and col1==col2:
            return 0
        
        if (row1+col1) == (row2+col2) or row1-col1 == row2-col2:
            return 1
        
        return 2
        
        
            
            
                    

                
                

                    
                
        
        return dfs(row1, col1)






    
    print(
        rook(row1, row2, col1, col2), 
        bishop(row1, row2, col1, col2), 
        king(row1, row2, col1, col2)
    )
                

            





            











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





