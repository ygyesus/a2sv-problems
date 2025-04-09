# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)

        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 0:
                    continue

                graph[row].append(col)

        count = 0
        visited = set()

        def dfs(city):
            visited.add(city)
            for neighbor in graph[city]:
                if neighbor not in visited:
                    dfs(neighbor)

        
        provinces = 0
        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces


            

