# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

from collections import defaultdict

n,k = map(int, input().split())

a = list(map(int, input().split()))

ans = a[-1] - a[0]

arr = [a[i] - a[i+1] for i in range(n-1) ]
arr.sort()

if n==k:
    print(0)
elif k==1:
    print(ans)
else:
    ans += sum(arr[:k-1])
    print(ans)
