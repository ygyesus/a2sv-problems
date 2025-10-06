# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def isAlmostPrime(num):
    temp = num
    factorization = set()
    for d in range(2, temp):
        if not d*d<=temp: break
        while num%d == 0:
            num //= d
            factorization.add(d)
            
    if num>1: factorization.add(num)
    return len(factorization) == 2


n = int(input())
ans = 0
for num in range(2, n+1):
    ans += isAlmostPrime(num)
print(ans)