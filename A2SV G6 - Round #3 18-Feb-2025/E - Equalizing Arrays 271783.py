# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

def solve():
    if sum(a) != sum(b):
        print(-1)
        return
    a_sum = b_sum = 0
    
    i=j=length=0
    
    while i<len(a):
        a_sum += a[i]
        b_sum += b[j]
        
        i+=1
        j+=1
        
        while a_sum != b_sum:
            if a_sum < b_sum:
                a_sum += a[i]
                i+=1
            else:
                b_sum += b[j]
                j+=1
                
        length += 1
        
        
    print(length)
        
    
n = int(input())

a = list(map(int, input().split()))

m = int(input())

b = list(map(int, input().split()))

solve()



