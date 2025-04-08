# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        graph = defaultdict(set)

        for x,y in edges:
            graph[x].add(y)
            graph[y].add(x)

        visited = set()

        def dfs(node):
            if node==destination:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            return False

        return dfs(source)
