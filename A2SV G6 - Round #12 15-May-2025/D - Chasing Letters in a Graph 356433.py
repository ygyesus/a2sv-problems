# Problem: D - Chasing Letters in a Graph - https://codeforces.com/gym/606404/problem/D

import threading
import sys
from math import floor, ceil, sqrt
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest
heappoppush = heapreplace
# nlargest(2, [5,6,7])
# Always Heapify first

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
    nodes, edges = INTS()
    s = input()
    graph = [
        [] for _ in range(nodes+1)
    ]
    incoming = [
        0 for _ in range(nodes+1)
    ]
    
    alphabets = [
        [0]*26 for _ in range(nodes+1)
    ]
    maxFreq = 1

    def getIndex(char):
        return ord(char) - ord('a')
    

    for _ in range(edges):
        node, neighbor = INTS()
        graph[node].append(neighbor)
        incoming[neighbor] += 1

    # DETECT CYCLE

    q = deque()
    for node in range(1, nodes+1):
        if incoming[node] == 0:
            q.append(node)

    visited = 0
    while q:
        node = q.popleft()
        visited += 1

        i = getIndex(s[node-1])
        alphabets[node][i] += 1
        maxFreq = max(maxFreq, alphabets[node][i])
        for neighbor in graph[node]:
            # if neighbor in visited:
            #     continue
            incoming[neighbor] -= 1
            parentFreq = alphabets[node]
            childFreq = alphabets[neighbor]

            for i in range(26):
                childFreq[i] = max(childFreq[i], parentFreq[i])
                maxFreq = max(maxFreq, childFreq[i])
                
            if incoming[neighbor] == 0:
                q.append(neighbor)


    if not visited == nodes:
        print(-1)
        return
    
    print(maxFreq)
    


    







def main():
    t = 1
    # t = int(input())
    for _ in range(t):
        solve()






#############################################################################





main()