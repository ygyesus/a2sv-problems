# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

from collections import defaultdict

t = int(input())

            
for _ in range(t):
    n,k = list(map(int, input().split()))
    
    graph = [
        [1 for _ in range(n)] for _ in range(n)
    ]
    
    visited = set()
    def dfs(node):
        
        visited.add(node)
        for neighbor in range(n):
            if graph[node][neighbor] == 0 or (neighbor in visited):
                continue
            
            dfs(neighbor)
            
    for row in range(n):
        if not k:
            break
        for col in range(n):
            if row==col:
                continue
            if not k:
                break
            
            if not graph[row][col]:
                continue
            
            graph[row][col] = 0
            graph[col][row] = 0
            k -= 1
    
#     print("==========")        
#     for row in graph:
#         print(row)
#     
            

    dfs(0)
    print(len(visited))
#     print(
            
        
        
