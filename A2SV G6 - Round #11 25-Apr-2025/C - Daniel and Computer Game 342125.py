# Problem: C - Daniel and Computer Game - https://codeforces.com/gym/604781/problem/C

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
    n,k = INTS()

    left = input()
    right = input()

    arr = [left, right]

    q = deque([(1, 0, 0)])
    visited = set()

    def isValid(level, water, x):
        
        if x[level-1] == 'X':
            return False
        
        if level <= water:
            return False
        return True

    total = 0
    while q:
        # print(q)
        level, water, i = q.pop()
        # print((level, water, i, arr[i%2]))
        visited.add((level, i))

        # if invalid, skip state
        if level<=n and (not isValid(level,water,arr[i%2])):
            continue
        
        elif level + 1 > n or level+k > n:
            print("YES")
            return
        
        if not (level+1,i) in visited:
            q.append((level+1, water+1, i))

        if not (level+k, (i+1)%2) in visited:
            q.append((level+k, water+1, (i+1)%2))

        if not (level-1,i) in visited:
            if level-1 >= 1:
                q.append((level-1, water+1, i))



    print("NO")

        
        




        

        






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