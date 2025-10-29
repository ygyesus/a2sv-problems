# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

words = []
for order1 in range(ord('a'), ord('z')+1):
    char1 = chr(order1)
    for order2 in range(ord('a'), ord('z')+1):
        char2 = chr(order2)
        if char1 == char2: continue
        word = char1 + char2
        words.append(word)

t = int(input())

for _ in range(t):
    s = input()
    
    print(1+words.index(s)) 