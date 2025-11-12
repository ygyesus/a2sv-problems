# Problem: Tram - https://codeforces.com/problemset/problem/116/A

n = int(input())

maxAns = ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    ans += (b-a)
    maxAns = max(maxAns, ans)
    
print(maxAns)