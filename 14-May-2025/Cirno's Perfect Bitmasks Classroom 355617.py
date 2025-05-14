# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())

for _ in range(t):
    x = int(input())
    y = 1
    
    while True:
        if x&y and x^y:
            print(y)
            break
        
        if x&(y+1) and x^(y+1):
            print(y+1)
            break      
        y <<= 1
        
