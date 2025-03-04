# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    reds = list(map(int, input().split()))

    m = int(input())
    blues = list(map(int, input().split()))

    maxRedTotal = redTotal = maxBlueTotal = blueTotal = 0
    
    for red in reds:
        redTotal += red
        maxRedTotal = max(maxRedTotal, redTotal)
        
    for blue in blues:
        blueTotal += blue
        maxBlueTotal = max(maxBlueTotal, blueTotal)
        
    print(maxRedTotal + maxBlueTotal)
    
