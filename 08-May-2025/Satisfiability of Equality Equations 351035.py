# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class UnionFind:
    def __init__(self, variables):
        self.root = {variable: variable for variable in variables}
        self.rank = {variable: 0 for variable in variables}

    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty: return

        rankx = self.rank[rootx]
        ranky = self.rank[rooty]

        if rankx > ranky:
            self.root[rooty] = rootx
        elif ranky > rankx:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
            

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        variables = set()

        for equation in equations:
            variables.add(equation[0])
            variables.add(equation[-1])

        dsu = UnionFind(variables)

        for equation in equations:
            a = equation[0]
            b = equation[-1]

            if equation[1:3] == '==':
                dsu.union(a,b)

        for equation in equations:
            a = equation[0]
            b = equation[-1]
            if equation[1:3] == '!=':
                if dsu.find(a) == dsu.find(b):
                    return False

        return True
                
