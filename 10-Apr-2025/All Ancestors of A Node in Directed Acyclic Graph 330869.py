# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        parents = defaultdict(list)

        for parent, child in edges:
            parents[child].append(parent)

        ans = [[] for _ in range(n)]


        visited = set()
        def dfs(childNode, parentNode):
            if childNode != parentNode:
                ans[childNode].append(parentNode)
            visited.add(parentNode)

            for parent in parents[parentNode]:
                # print(parent)
                # print()
                # print(visited)
                if parent in visited:
                    continue

                dfs(childNode, parent)

            
        for childNode in range(n):
            visited = set()

            dfs(childNode, childNode)
            if ans[childNode]:
                ans[childNode].sort()

        # print(ans)
        return ans
            



            

        

        
        