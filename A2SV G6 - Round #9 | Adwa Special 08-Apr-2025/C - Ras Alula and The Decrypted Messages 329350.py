# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/601269/problem/C

t = int(input())

for _ in range(t):
    n,m = list(map(int, input().split()))
    s = list(input())
    
    for i in range(n):
        s[i] = ord(s[i])
        
    w = list(input())
    
    for i in range(m):
        w[i] = ord(w[i])
        
    target = sum(w)
    
    total = sum(s[:m])
    if total == target:
        print("YES")
        continue
    flag = False
    left = 0
    for right in range(m, n):
        total += s[right]
        total -= s[left]
        if total == target:
            flag = True
            break
        left += 1
        
    if flag:
        print("YES")
    else:
        print("NO")
    
    
    
    
    
