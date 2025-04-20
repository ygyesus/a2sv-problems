# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D


def isCharGood(s, char):
    n = len(s)
    if len(s) == 1:
        if s==char:
            return 0
        return 1
    
    
    mid = n//2
    minimum = float('inf')
    nextChar = chr(ord(char)+1)
    
    localMin = mid-s[:mid].count(char)
    localMin += isCharGood(s[mid:], nextChar)
    minimum = min(minimum, localMin)
    
    localMin = (n-mid)-s[mid:].count(char)
    localMin += isCharGood(s[:mid], nextChar)
    minimum = min(minimum, localMin)
    
    return minimum

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    char = 'a'
    ans = isCharGood(s, char)
    print(ans)
    
    
    
