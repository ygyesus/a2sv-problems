# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

t = int(input())

def check(penalty, s, a, k):
    ans = []
    for i, char in enumerate(s):
        if a[i] > penalty:
            ans.append(s[i])
        else:
            ans.append(None)

    soFar = 'R'
    ops = 0
    for char in ans:
        if soFar == 'R':
            if char == 'B':
                soFar = 'B'
                ops += 1
        elif soFar == 'B':
            if char == 'R':
                soFar = 'R'

    return ops <= k

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    a = list(map(int, input().split()))
    

    left, right = 0, max(a)
    penalty = None

    while left <= right:
        mid = (left + right) // 2
        if check(mid, s, a, k):  # Pass k to check
            penalty = mid
            right = mid - 1
        else:
            left = mid + 1

    print(penalty if penalty is not None else 0)
#     print("===")
