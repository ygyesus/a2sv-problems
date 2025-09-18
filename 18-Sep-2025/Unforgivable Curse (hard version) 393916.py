# Problem: Unforgivable Curse (hard version) - https://codeforces.com/contest/1800/problem/E2

from collections import defaultdict, Counter

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        
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
    
    


t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    
    s = input()
    t = input()
    
    dsu = UnionFind(n)
    for i in range(n):
        c, d = i+k, i+(k+1)
        
        for index in [c, d]:
            if not 0<=index<n: continue
            dsu.union(i, index)
            
#     print(dsu.root)
#     continue
            
    rootToIndices = defaultdict(list)
    valid = True
    
    for i in range(n):
        char = s[i]
        root = dsu.find(i)
        indices = rootToIndices[root]
        indices.append(i)
        
#     print(rootToIndices)
    for root in rootToIndices:
#         print("indices:", rootToIndices[root])
        if not valid: break
        counter_s = Counter()
        counter_t = Counter()
        
        for index in rootToIndices[root]:
#             print("index:", index)
            char_s, char_t = s[index], t[index]
            counter_s[char_s] += 1
            counter_t[char_t] += 1
#         print("COUNTER_S:", counter_s)
#         print("COUNTER_T:", counter_t)
        if counter_s != counter_t:
            valid = False
            break
            
        
    if valid: print("YES")
    else: print("NO")
            
        
            
        
    
            
    
    
