# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

rows, cols = map(int, input().split())

grid = [
    ['.' for _ in range(cols)] for _ in range(rows)
]
for row in range(0, rows, 2):
    
    for col in range(cols):
        grid[row][col] = '#'
        
right = True
for row in range(1, rows, 2):
    if right: grid[row][-1] = '#'
    else: grid[row][0] = '#'
    right = not right
    
for ROW in grid: print(''.join(ROW))