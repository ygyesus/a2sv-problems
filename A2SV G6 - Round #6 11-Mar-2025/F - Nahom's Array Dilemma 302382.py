# Problem: F - Nahom's Array Dilemma - https://codeforces.com/gym/594077/problem/F

t = int(input())

def check(arr):

    n = len(arr)
    stack = []

    total = 0

    prefix = [0]
    
    for i in range(n):
        prefix.append(prefix[-1] + arr[i])

    # print(prefix)


    for right in range(n):
        while stack and arr[stack[-1]] <= arr[right]:
            left = stack.pop()

            total = prefix[right+1] - prefix[left]

            if total > arr[right]:
                return False

        stack.append(right)

    return True
       
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if check(a) and check(a[::-1]):
        print("YES")
    else:
        print("NO")
    
    