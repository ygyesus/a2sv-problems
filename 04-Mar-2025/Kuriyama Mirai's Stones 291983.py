# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B


def calculatePrefix(arr):
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]
        
    return arr

n = int(input())

costs = list(map(int, input().split()))
sortedCosts = sorted(costs)

prefixSortedCosts = calculatePrefix(sortedCosts)
prefixCosts = calculatePrefix(costs)

m = int(input())

for __ in range(m):
    TYPE, l, r = map(int, input().split())
    l -= 1
    r -= 1
    if TYPE == 1:
        if l==0:
            print(prefixCosts[r])
        else:
            print(prefixCosts[r] - prefixCosts[l-1])
            
    elif TYPE == 2:
        if l==0:
            print(prefixSortedCosts[r])
        else:
            print(prefixSortedCosts[r] - prefixSortedCosts[l-1])
            
        
    
