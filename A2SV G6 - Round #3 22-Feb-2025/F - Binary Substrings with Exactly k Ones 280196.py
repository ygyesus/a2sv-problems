# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

def findAtmost(k):
    if k==-1:
        return 0
    left = 0
    
    total = 0
    ans = 0
    for right in range(len(s)):
        total += int(s[right])
        
        while total > k:
            total -= int(s[left])
            left += 1
            
        ans += right-left+1
        
    return ans
k = int(input())

s = input()

print(findAtmost(k) - findAtmost(k-1))
