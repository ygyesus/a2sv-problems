# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

from collections import defaultdict

n = int(input())

pointFreq = defaultdict(int)




for _ in range(n):
    start, end = map(int, input().split())
    
    pointFreq[start] += 1
    pointFreq[end+1] -= 1
     
# print("pointFreq:", dict(pointFreq))
points = list(pointFreq.keys())
points.sort()

pointFreq = [pointFreq[point] for point in points]

for i in range(1, len(pointFreq)):
    pointFreq[i] += pointFreq[i-1]
    

ans = defaultdict(int)
for i in range(len(points)-1):
    start = points[i]
    end = points[i+1]
    
    
    ans[pointFreq[i]] += end-start
    
# print("ans:", dict(ans))
# print(points)
# print(pointFreq)
# freqFrequency...



ans = [ans[i] for i in range(1,n+1)]
print(*ans)
    
    
# print("points:", points)
# print("pointFreq:", pointFreq)


   
