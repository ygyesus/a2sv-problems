# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        incoming = defaultdict(int)

        for node, neighbor in edges:
            graph[node].append(neighbor)
            graph[neighbor].append(node)

            incoming[node] += 1
            incoming[neighbor] += 1

        
        q = deque()


        for num in range(n):
            if incoming[num] == 1:
                q.append(num)

        visited = set()
        ans = [x for x in range(n)]

        while q:
            ans = list(q)
            for _ in range(len(q)):
                node = q.popleft()
                visited.add(node)

                for neighbor in graph[node]:
                    if neighbor in visited: continue
                    incoming[neighbor] -= 1

                    if incoming[neighbor] == 1:
                        q.append(neighbor)

        return ans