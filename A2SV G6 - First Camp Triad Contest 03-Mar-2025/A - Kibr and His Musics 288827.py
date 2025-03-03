# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

n,m = map(int, input().split())

prefix = []
for i in range(n):
    c,t = map(int, input().split())
    
    prefix.append(c*t)
    if i>0:
        prefix[i] += prefix[i-1]
    
    
moments = list(map(int, input().split()))

songIndex = 0
for j in range(m):
    
    moment = moments[j]    
    while prefix[songIndex]<moment:
        songIndex += 1
        
    print(songIndex+1)
        
    
