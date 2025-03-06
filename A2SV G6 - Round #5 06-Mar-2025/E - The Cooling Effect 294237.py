# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

t = int(input())
input()
def func(forwardTemps):
    minTempSoFar = float('inf')
    lastMinTempIndex = 0
    
    for i in range(len(forwardTemps)):

        if forwardTemps[i] < minTempSoFar + abs(i-lastMinTempIndex):
            minTempSoFar = forwardTemps[i]
            lastMinTempIndex = i
            
        currTemp = minTempSoFar + abs(i-lastMinTempIndex)
        
        forwardTemps[i] = currTemp
for _ in range(t):
    n,k = map(int, input().split())
    conditionerIndices = list(map(int, input().split()))
    conditionerIndices = list(map(lambda x: x-1, conditionerIndices))
    
    conditionerTemps = list(map(int, input().split()))
    if _ < t-1:
        input()
    forwardTemps = [float('inf') for i in range(n)]
    backwardTemps = [x for x in forwardTemps]

    
    for i,conditionerIndex in enumerate(conditionerIndices):
        forwardTemps[conditionerIndex] = conditionerTemps[i]
        backwardTemps[conditionerIndex] = conditionerTemps[i]
            
    backwardTemps = backwardTemps[::-1]
    func(forwardTemps)
    func(backwardTemps)
    backwardTemps = backwardTemps[::-1]

    ans = []
    
    for i in range(n):
        minimum = min(forwardTemps[i], backwardTemps[i])
        ans.append(minimum)
#     print()        
    print(*ans)
            


