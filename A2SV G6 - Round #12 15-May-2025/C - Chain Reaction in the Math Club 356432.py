# Problem: C - Chain Reaction in the Math Club - https://codeforces.com/gym/606404/problem/C

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
    # students = n, laces = m
    n,m = INTS()

    graph = defaultdict(set)
    incoming = defaultdict(int)

    for _ in range(m):
        a,b = INTS()
        graph[a].add(b)
        graph[b].add(a)

        incoming[a] += 1
        incoming[b] += 1

    # print(dict(incoming))

    q = deque()
    for student in incoming:
        if incoming[student] == 1:
            q.append(student)

    groups = 0
    # print(list(q))
    
    while q:
        # print(list(q))
        flag = False


        for _ in range(len(q)):
            kicked = q.popleft()
            if incoming[kicked] == 1:
                flag = True
            else:
                continue

            for neighbor in graph[kicked]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 1:
                    q.append(neighbor)
                

            # print("new incoming:", dict(incoming))

        
        if flag:
            groups += 1

    print(groups)








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