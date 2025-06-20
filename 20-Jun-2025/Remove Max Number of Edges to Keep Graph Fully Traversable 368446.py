# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:

    def __init__(self, n):
        self.root = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]

    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return x

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)

        if rootx == rooty: return

        rankx, ranky = self.rank[rootx], self.rank[rooty]

        if rankx>ranky:
            self.root[rooty] = rootx
        elif ranky>rankx:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        

        edges.sort(key = lambda trio: -trio[0])
        alice = UnionFind(n)
        bob = UnionFind(n)

        ans = 0
        for TYPE, node, neighbor in edges:
            if TYPE == 3:
                if alice.find(node) == alice.find(neighbor) and bob.find(node)==bob.find(neighbor):
                    ans += 1
                else:
                    alice.union(node, neighbor)
                    bob.union(node, neighbor)

                continue

            if TYPE == 1:
                if alice.find(node)==alice.find(neighbor):
                    ans += 1
                else:
                    alice.union(node, neighbor)
                
                continue

            if TYPE == 2:
                if bob.find(node)==bob.find(neighbor):
                    ans += 1
                else:
                    bob.union(node, neighbor)


        aliceRoots = {alice.find(node) for node in range(1, n+1)}
        bobRoots = {bob.find(node) for node in range(1, n+1)}

        if len(aliceRoots) + len(bobRoots) > 2: return -1
        return ans