# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

k = int(input())
s = input()


kMinusOneAtMost = 0
kAtMost = 0
left = 0
totalOnes = 0


# k-1 at most
for right in range(len(s)):
    if k-1 < 0:
        break
    char = s[right]
    
    if char == '1':
        totalOnes += 1
        
    while totalOnes > k-1:
        if s[left] == '1':
            totalOnes -= 1
            
        left += 1
        
    kMinusOneAtMost += right-left+1
    
left = 0
totalOnes = 0
# k at most
for right in range(len(s)):
    char = s[right]
    
    if char == '1':
        totalOnes += 1
        
    while totalOnes > k:
        if s[left] == '1':
            totalOnes -= 1
            
        left += 1
        
    kAtMost += right-left+1
    

print(kAtMost - kMinusOneAtMost)
