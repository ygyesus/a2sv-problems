# Problem: E - Simple Cycle With Minimal Lightest Edge - https://codeforces.com/gym/607625/problem/E

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

class UnionFind:
    def __init__(self, nodes):
        self.root = {node:node for node in nodes}
        self.rank = {node:0 for node in nodes}

    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return self.root[x]
    
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx==rooty: return


        rankx, ranky = self.rank[rootx], self.rank[rooty]

        if rankx >= ranky:    
            self.root[rooty] = rootx
            if rankx > ranky:
                self.rank[rooty] += 1
        else:
            self.root[rootx] = rooty


def solve():
    nodes, edges = INTS()
    minWeight = float('inf')
    graph = defaultdict(list)
    allEdges = []
    nodes = set()
    for _ in range(edges):
        node, neighbor, weight = INTS()
        allEdges.append((weight, node, neighbor))
        graph[node].append(neighbor)
        graph[neighbor].append(node)
        nodes.add(node)
        nodes.add(neighbor)

    dsu = UnionFind(nodes)
    allEdges.sort(key = lambda x: -x[0])

    start = None
    for weight, node, neighbor in allEdges:
        if dsu.find(node) == dsu.find(neighbor):
            minWeight = min(minWeight, weight)
            start = (node, neighbor)
        else:
            dsu.union(node, neighbor)



    path = []
    visited = set()

    node, neighbor = start
    graph[neighbor].remove(node)
    graph[node].remove(neighbor)

    '''
    Store the cycle in reverse order, starting from neighbor (start[1])
    Skip node (start[0])
    start == (node, neighbor) == start edge
    '''
    def dfs(node):
        visited.add(node)
        if node == start[0]:
            return True
        for neighbor in graph[node]:
            if neighbor in visited: continue
            if dfs(neighbor):
                path.append(node)
                return True
            
        
        return False
        
    dfs(neighbor)
    path.append(start[0])
    path = path[::-1]

    print(minWeight, len(path))
    print(*path)


        







    

    






def main():
    t = 1
    t = int(input())
    for _ in range(t):
        solve()







#############################################################################


isRecursion = True



def recursion():
   if __name__ == '__main__':
       sys.setrecursionlimit(1 << 30)
       threading.stack_size(1 << 22)

       main_thread = threading.Thread(target=main)
       main_thread.start()
       main_thread.join()




if isRecursion:
   recursion()
else:
   main()