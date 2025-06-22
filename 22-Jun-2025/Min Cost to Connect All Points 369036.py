# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:

    def __init__(self, nodes):
        self.root = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return x

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx==rooty: return

        rankx, ranky = self.rank[rootx], self.rank[rooty]

        if rankx>ranky:
            self.root[rooty] = rootx
        elif ranky>rankx:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        points = [tuple(point) for point in points]
        def distance(twoDuos):
            duo1, duo2 = twoDuos
            x1, y1 = duo1
            x2, y2 = duo2
            return abs(x2-x1) + abs(y2-y1)

        twoPoints = []

        visited = defaultdict(set)
        for pointOne in points:
            for pointTwo in points:
                if pointTwo in visited[pointOne]: continue
                
                visited[pointOne].add(pointTwo)
                visited[pointTwo].add(pointOne)
                if pointOne==pointTwo: continue

                twoPoints.append((pointOne, pointTwo))


        twoPoints.sort(key = lambda twoDuos: distance(twoDuos))
        dsu = UnionFind(points)
        total = 0
        for duo1, duo2 in twoPoints:

            if dsu.find(duo1) == dsu.find(duo2): continue
            dsu.union(duo1, duo2)
            total += distance((duo1, duo2))

        return total

        