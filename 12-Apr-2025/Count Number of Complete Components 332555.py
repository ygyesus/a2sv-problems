# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        connectedComponent = set()
        visited = set()
        
        def dfs(node):
            visited.add(node)
            connectedComponent.add(node)
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue

                dfs(neighbor)

        connectedComponents = []

        for node in range(n):
            if node in visited:
                continue
            connectedComponent = set()
            dfs(node)
            connectedComponents.append(connectedComponent)

        ans = 0
        for connectedComponent in connectedComponents:
            flag = True
            for a in connectedComponent:
                for b in connectedComponent:
                    if a==b:
                        continue

                    if not b in graph[a]:
                        flag = False
                        break

                if not flag:
                    break

            if flag:
                ans += 1

        return ans