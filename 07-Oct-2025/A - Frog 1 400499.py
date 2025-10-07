# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())
h = list(map(int, input().split()))

dp = [0 for _ in range(n+1)]
h.insert(0, 0)

if 2<=n:
    dp[2] = abs(h[2] - h[1])
    
for i in range(3, n+1):
    diff2 = abs(h[i] - h[i-2])
    diff1 = abs(h[i] - h[i-1])
    
    prev1 = dp[i-1]
    prev2 = dp[i-2]
    
    dp[i] = min(prev1+diff1, prev2+diff2)
    
print(dp[n])