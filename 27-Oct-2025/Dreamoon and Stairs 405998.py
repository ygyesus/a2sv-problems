# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

totalSteps, moveFactor = map(int, input().split())

def isValid(moves):
    if not moves%moveFactor == 0: return False
    
    return 1*moves <= totalSteps <= 2*moves


left, right = 0, 10**4

ans = -1
while left<=right:
    k = (left+right)//2
    moves = moveFactor*k
    if isValid(moves):
        ans = moves
        right = k-1
    elif 2*moves < totalSteps:
        left = k+1
    elif totalSteps < moves:
        right = k-1
        
print(ans)