# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:

    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, x):

        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return self.root[x]

    def union(self, x, y):

        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty: return

        rankx, ranky = self.rank[rootx], self.rank[rooty]
        if rankx > ranky:
            self.root[rooty] = rootx
        elif ranky > rankx:
            self.root[rootx] = rooty
        elif rankx==ranky:
            self.root[rooty] = rootx
            self.rank[rootx] += 1

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        dsu = UnionFind(n)
        original = deepcopy(queries)
        queries.sort(key = lambda query: query[-1])
        edgeList.sort(key = lambda edge: edge[-1])

        ans = {}

        edge = 0
        
        for query in queries:
            # while cost < limit:
            while edge < len(edgeList) and edgeList[edge][-1] < query[-1]:
                dsu.union(edgeList[edge][0], edgeList[edge][1])
                edge += 1

            ans[tuple(query)] = dsu.find(query[0])==dsu.find(query[1])

        ans = [ans[tuple(query)] for query in original]
        return ans

                



