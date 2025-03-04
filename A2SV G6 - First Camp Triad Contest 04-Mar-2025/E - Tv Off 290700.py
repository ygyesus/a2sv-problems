# Problem: E - Tv Off - https://codeforces.com/gym/589822/problem/E

from collections import Counter, defaultdict
n = int(input())

duos = []

moments = defaultdict(int)
for _ in range(n):
    l,r = map(int, input().split())
    
    moments[l] += 1
    moments[r] += 0
    moments[r+1] -= 1
    duos.append((l,r))

momentList = list(moments.keys())
momentList.sort()

prefix = [moments[moment] for moment in momentList]

for i in range(1, len(prefix)):
    prefix[i] += prefix[i-1]
    
# momentList
# prefix

indexOfMoment = {}
# print("PREFIX:", prefix)
for i in range(len(momentList)):
    moment = momentList[i]
        
    moments[moment] = prefix[i]
    indexOfMoment[moment] = i
    


found = False
    
# print("MOMENTS:", dict(moments))
# print("indexOfMoment:", indexOfMoment)
for i, (l,r) in enumerate(duos):
    if moments[l] > 1 and moments[r] > 1:
        flag = True
        for j in range(indexOfMoment[l], indexOfMoment[r]+1):
            moment = momentList[j]
            if not moments[moment] > 1:
                flag = False
                break
            
        if flag:
#             print("INDEX:", i, "	DUO:", (l,r))
            found = True
            print(i+1)
            break

if not found:
    print(-1)
    


