# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        greater = defaultdict(list)

        quietValueToNode = {}

        for node, quietValue in enumerate(quiet):
            quietValueToNode[quietValue] = node

        for g,l in richer:
            greater[l].append(g)

        visited = {}

        def dfs(node):
            # print(node, dict(greater))

            minQuiet = quiet[node]

            for neighbor in greater[node]:
                if neighbor in visited:
                    neighborMinQuiet = visited[neighbor]
                else:
                    neighborMinQuiet = dfs(neighbor)

                minQuiet = min(minQuiet, neighborMinQuiet)
            
            if not node in visited: visited[node] = minQuiet
            # print("VISITED:", visited, node)

            return minQuiet

        for node in range(len(quiet)):
            dfs(node)

        for node in visited:
            quietValue = visited[node]

            visited[node] = quietValueToNode[quietValue]

        # print("=====================")
        # print(visited)

        ans = []
        for node in range(len(quiet)):
            ans.append(visited[node])

        return ans