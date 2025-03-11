# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

def solve(string):

    indexToSubseq = {}
    ones, zeroes = [], []
    maximum = 0
    

    for i, char in enumerate(string):
        if char == '0':
            if ones:
                x = ones.pop()
                zeroes.append(x)
                indexToSubseq[i] = x
            else:
                maximum += 1
                zeroes.append(maximum)
                indexToSubseq[i] = maximum
                
        elif char == '1':
            if zeroes:
                x = zeroes.pop()
                ones.append(x)
                indexToSubseq[i] = x

            else:
                maximum += 1
                ones.append(maximum)
                indexToSubseq[i] = maximum
                
        
    print(maximum)
    arr = [indexToSubseq[i] for i in range(n)]
    print(*arr)
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    solve(s)
