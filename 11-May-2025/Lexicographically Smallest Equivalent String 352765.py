# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:

    def __init__(self, nodes):
        self.root = {node:node for node in nodes}
        self.rank = {node:0 for node in nodes}
    def find(self, x):
        if not x in self.root: return x
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty: return

        self.root[rootx] = self.root[rooty] = min(rootx, rooty)
        return
        # rankx, ranky = self.rank[rootx], self.rank[rooty]

'''
        if rankx > ranky:
            self.root[rooty] = rootx
        elif ranky > rankx:
            self.root[rootx] = rooty
        else:
            self.root[rootx] = self.root[rooty] =
            self.rank[rootx] += 1
'''

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        nodes = set()
        for char in s1:
            nodes.add(char)
        for char in s2:
            nodes.add(char)

        # for char in base

        dsu = UnionFind(nodes)

        for i in range(len(s1)):
            dsu.union(s1[i], s2[i])

        ans = ""
        for char in baseStr:
            root = dsu.find(char)
            ans += root

        return ans
