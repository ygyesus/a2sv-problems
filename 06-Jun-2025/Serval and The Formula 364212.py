# Problem: Serval and The Formula - https://codeforces.com/problemset/problem/2085/C

t = int(input())

for _ in range(t):
    
    x,y = list(map(int, input().split()))
    
    if x==y: print(-1)
    else:
        maxNum = max(x,y)
        bitLength = 0
        
        while maxNum>>bitLength:
            bitLength += 1
            
        maxNum = 2**(bitLength+1)
        
        print(maxNum-max(x,y))        