# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node, edge):
            visited.add(node)

            for neighbor in graph[node]:

                if neighbor in visited:
                    continue

                if [node, neighbor] == edge or [neighbor, node] == edge:
                    continue

                dfs(neighbor, edge)

        edges = edges[::-1]

        for edge in edges:
            visited = set()
            dfs(edge[0], edge)

            if len(visited) == len(graph):
                return edge

        
