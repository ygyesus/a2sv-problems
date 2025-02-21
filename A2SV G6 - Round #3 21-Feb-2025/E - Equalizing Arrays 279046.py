# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

i=j=0
flag = True

a_sum = b_sum = 0
length = 0
if sum(a) != sum(b):
    flag = False
while i<len(a) and flag:

    a_sum += a[i]
    b_sum += b[j]
    
    i+=1
    j+=1
    
    while a_sum != b_sum:
        while a_sum < b_sum:
            a_sum += a[i]
            i+=1
         

        while b_sum < a_sum:
            b_sum += b[j]
            j+=1
        
    length += 1
    
if not flag:
    print(-1)
else:
    print(length)
