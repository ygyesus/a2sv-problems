# Problem: D - Merbebt and Maze - https://codeforces.com/gym/604781/problem/D

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
    LIST()
    n,k = INTS()
    friends = INTS()

    friends = [friend-1 for friend in friends]

    
    merbebt = [0]

    graph = [
        [] for _ in range(n)
    ]


    for _ in range(n-1):
        node, neighbor = INTS()
        node -= 1
        neighbor -= 1

        graph[node].append(neighbor)
        graph[neighbor].append(node)

    terminalNodes = {node for node in range(n) if len(graph[node])==1}

    # if 0 in terminalNodes and not(graph[0][0] in terminalNodes):
    #     print("YES")
    #     return
    
    friends = deque(friends)
    merbebt = deque(merbebt)

    def bfs(q):
        
        distance = 0
        minDistance = {x: 0 for x in q}

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                minDistance[node] = distance


                for neighbor in graph[node]:
                    if neighbor in minDistance:
                        continue
                    minDistance[neighbor] = distance+1
                    q.append(neighbor)

            distance += 1

        return minDistance
    
    friends = bfs(friends)
    merbebt = bfs(merbebt)

    for node in terminalNodes:
        if node==0:
            continue

        if merbebt[node]<friends[node]:
            print("YES")
            return
        
    print("NO")


    






def main():
    t = 1
    t = int(input())
    for _ in range(t):
        solve()
        # print("--------------------------------------------")






#############################################################################





if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()