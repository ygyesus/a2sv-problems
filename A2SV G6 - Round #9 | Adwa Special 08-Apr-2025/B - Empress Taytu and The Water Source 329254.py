# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/601269/problem/B

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

    demands = INTS()
    times = INTS()

    def calculate(wagon):
        if not wagon: 
            return -1

        hours = 0
        for i,demand in enumerate(demands):
            rounds = demand//wagon
            if demand%wagon:
                rounds += 1

            hours += rounds * times[i]
            if hours > k:
                return -1
            
        return hours
    
    left = 0
    right = 10**20

    ans = -1
    while left<=right:
        wagon = (left+right)//2

        if calculate(wagon) != -1:
            ans = wagon
            right = wagon-1

        else:
            left = wagon+1

    print(ans)
            





def main():
    t = 1
    t = int(input())
    for _ in range(t):
        solve()







#############################################################################





if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()