# Problem: B - Distribute - https://codeforces.com/gym/606404/problem/B

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
    n = INT()
    a = INTS()
    for i in range(len(a)):
        a[i] = (a[i], i)

    a.sort()

    left, right = 0,len(a)-1

    while left<right:
        
        leftNum, left_i = a[left]
        rightNum, right_i = a[right]

        print(left_i+1, right_i+1)
        left += 1

        right -= 1







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