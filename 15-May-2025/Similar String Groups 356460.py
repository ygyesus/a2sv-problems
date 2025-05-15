# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class UnionFind:
    def __init__(self, strings):
        self.root = {string: string for string in strings}
        self.rank = {string: 0 for string in strings}

    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty: return

        rankx, ranky = self.rank[x], self.rank[y]
        if rankx >= ranky:
            self.root[rooty] = rootx
            if rankx > ranky:
                self.rank[rootx] += 1
        elif ranky > rankx:
            self.root[rootx] = rooty


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        def condition(s1, s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
                    if diff > 2: return False
            return True

        dsu = UnionFind(strs)

        for i in range(len(strs)):
            s1 = strs[i]
            for j in range(len(strs)):
                s2 = strs[j]
                if condition(s1, s2): 
                    dsu.union(s1, s2)
    
        return len(set([dsu.find(x) for x in strs]))


