# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

i = j = 0

for j in range(m):
    while i<n and a[i] < b[j]:
        i += 1
        
    print(i, end = ' ')