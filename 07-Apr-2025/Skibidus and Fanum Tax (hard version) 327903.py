# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

t = int(input())

for _ in range(t):
    n,m = list(map(int, input().split()))

    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    flag = True
    
    a[0] = min(a[0], b[0] - a[0])
    
    for i in range(1, n):
        
        left, right = 0, m-1
        ans = a[i] if a[i] >= a[i-1] else None
        while left<=right:
            mid = (left+right)//2
            
            diff = b[mid] - a[i]
            if diff >= a[i-1]:
                if ans == None:
                    ans = diff
                else:
                    ans = min(ans, diff)
                right = mid-1
            else:
                left = mid+1
                
        if ans == None:
            flag = False
            break
        
        a[i] = ans
        
    if flag:
        print("YES")
    else:
        print("NO")