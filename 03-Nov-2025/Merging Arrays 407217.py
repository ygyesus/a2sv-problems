# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

[n, m] = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []

a_index = b_index = 0

while a_index<n and b_index<m:
    if a[a_index] < b[b_index]:
        c.append(a[a_index])
        a_index += 1
        
    else:
        c.append(b[b_index])
        b_index += 1
        
while a_index<n:
    c.append(a[a_index])
    a_index += 1
    
while b_index < m:
    c.append(b[b_index])
    b_index += 1
    
for member in c:
    print(member, end=" ")
