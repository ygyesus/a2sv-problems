# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        incoming = {}
        dependentsOf = defaultdict(list)
        for node in range(n):
            incoming[node] = len(graph[node])

            for neighbor in graph[node]:
                dependentsOf[neighbor].append(node)

        

        q = deque()
        
        for node in incoming:
            if incoming[node] == 0:
                q.append(node)

        visited = set()
        
        while q:
            # print(list(q))
            node = q.popleft()
            visited.add(node)

            for neighbor in dependentsOf[node]:
                # if neighbor in visited: continue
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    q.append(neighbor)

        return sorted(list(visited))

        


