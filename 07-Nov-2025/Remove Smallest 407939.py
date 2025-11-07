# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n==1:
        print("YES")
        return
    a.sort()
    
    for i in range(1, n):
        if not a[i] - a[i-1] <= 1:
            print("NO")
            return
        
    print("YES")
            

t = int(input())

for _ in range(t):
    solve()    