# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

[n,k,q] = list(map(int, input().split()))

prefix = [0] * 200001

for _ in range(n):
    left, right = map(int, input().split())
    
    prefix[left] += 1
    
    if right+1<len(prefix):
        prefix[right+1] -= 1
        
# print(prefix[90:101])
array = [0] * len(prefix)

for i in range(1, len(prefix)):
    prefix[i] += prefix[i-1]
for i in range(len(prefix)):
    if prefix[i] >= k:
        array[i] = 1
        
for i in range(1, len(array)):
    array[i] += array[i-1]
    
for _ in range(q):
    a, b = map(int, input().split())
#     print(array[a-1:b+2])
    print(array[b] - array[a-1])
    
    
