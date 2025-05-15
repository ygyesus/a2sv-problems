# Problem: E - Direct Without Regret - https://codeforces.com/gym/606404/problem/E

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
    
    incoming = defaultdict(int)
    graph = defaultdict(set)
    allNodes = set()

    directed = []

    undirected = []
    topSort = []
    for _ in range(edges):
        TYPE, node, neighbor = INTS()
        if TYPE == 1:
            incoming[neighbor] += 1
            graph[node].add(neighbor)
            directed.append((node, neighbor))
        
        else:
            undirected.append((node, neighbor))

        allNodes.add(node)
        allNodes.add(neighbor)

    q = deque()
    for node in allNodes:
        if incoming[node] == 0:
            q.append(node)

    visited = set()
    while q:
        node = q.popleft()
        visited.add(node)
        topSort.append(node)
        for neighbor in graph[node]:
            incoming[neighbor] -= 1
            if incoming[neighbor] == 0:
                q.append(neighbor)

    if len(visited) != len(allNodes):
        print("NO")
        return
    indices = {}

    for i, node in enumerate(topSort):
        indices[node] = i


    print("YES")
    for duo in directed:
        print(*duo)

    for duo in undirected:
        duo = list(duo)
        duo.sort(key = lambda x: indices[x])

        print(*duo)
    
    


   




    
   


    # print(minWeight)





def main():
    t = 1
    t = int(input())
    for _ in range(t):
        solve()







#############################################################################


isRecursion = False



def recursion():
   if __name__ == '__main__':
       sys.setrecursionlimit(1 << 30)
       threading.stack_size(1 << 27)

       main_thread = threading.Thread(target=main)
       main_thread.start()
       main_thread.join()




if isRecursion:
   recursion()
else:
   main()