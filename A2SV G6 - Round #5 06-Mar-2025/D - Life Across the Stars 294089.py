# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict

n = int(input())

datesToFreq = defaultdict(int)
for _ in range(n):
    b,d = map(int, input().split())
    
    datesToFreq[b] += 1
    datesToFreq[d] -= 1
    
    
dates = datesToFreq.keys()
dates = sorted(list(dates))

freqs = [datesToFreq[date] for date in dates]
for i in range(1, len(freqs)):
    freqs[i] += freqs[i-1]
    
maxFreq = 0
maxDate = -1

for i,freq in enumerate(freqs):
    if freq > maxFreq:
        maxFreq = freq
        maxDate = dates[i]
    
print(maxDate, maxFreq)
    
