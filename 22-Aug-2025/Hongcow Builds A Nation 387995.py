# Problem: Hongcow Builds A Nation - https://codeforces.com/contest/744/problem/A

visited = set()

def dfs(node):
    visited.add(node)
    count = 1
    for neighbor in graph[node]:
        if neighbor in visited: continue
        count += dfs(neighbor)
        
    return count
    

nodes, edges, k = map(int, input().split())

govs = set(map(int, input().split()))

graph = [[node] for node in range(nodes+1)]

for _ in range(edges):
    node, neighbor = map(int, input().split())
    
    graph[node].append(neighbor)
    graph[neighbor].append(node)

maxCitizens = -1
maxGov = -5

totalEdges = 0

citizenCounts = []

for govNode in govs:
    citizens = dfs(govNode)
    if citizens>maxCitizens:
        maxCitizens = citizens
        maxGov = govNode
    citizenCounts.append(citizens)

neutrals = 0
for neutral in range(1, nodes+1):
    if neutral not in visited:
        neutrals += 1
        
citizenCounts.sort()
citizenCounts[-1] += neutrals

for citizenCount in citizenCounts:
    totalEdges += (citizenCount) * (citizenCount-1)//2
    
    
# print("GRAPH:", graph)
# print("GOVS:", govs)
# print("NEUTRALS:", neutrals, "maxCitizens:", maxCitizens)
# totalEdges += neutrals * maxCitizens

print(totalEdges-edges)
