# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

from collections import Counter
t = int(input())
for _ in range(t):
    counter = Counter()

    n = int(input())
    
    a = list(map(int, input().split()))
    
    for i in range(n):
#         print(bin(a[i])[2:])
        
        bitLength = 0
        while a[i]>>bitLength:
            counter[bitLength] += a[i]>>bitLength & 1
            bitLength += 1
            
    ans = []
#     print(dict(counter))
    for k in range(1, n+1):
        flag = True
        for bitLength in counter:
            if counter[bitLength]%k:
                flag = False
                break
            
        if flag:
            ans.append(k)
            
    print(*ans)
        
    
    
    
