# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

t = int(input())

for _ in range(t):
    n,q = list(map(int, input().split()))
    
    a = list(map(int, input().split()))
    prefix = [0]
    
    for i in range(n):
        prefix.append(prefix[-1] + a[i])
    
    for _ in range(q):
        l,r,k = list(map(int, input().split()))
        l-=1
        r-=1
        
        leftSum = prefix[l]
        rightSum = prefix[-1] - prefix[r+1]
        
        midSum = k*(l-r+1)
        
        if (leftSum+midSum+rightSum) % 2:
            print("YES")
        else:
            print("NO")
        
        
