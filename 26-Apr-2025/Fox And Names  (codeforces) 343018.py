# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, Counter, deque

n = int(input())

names = []

graph = defaultdict(list)
incoming = defaultdict(int)

def compare(x,y):
#     print((x,y))
    i=j=0
    
    while i<len(x) and j<len(y):
        char_i = x[i]
        char_j = y[j]
        
        if char_i != char_j:
            graph[char_i].append(char_j)
            incoming[char_j] += 1
#             print(incoming)
            return True
        
        i+=1
        j+=1
        
    if len(x) > len(y): return False
    return True
        
    

for _ in range(n):
    
    name = input()
    names.append(name)
    
flag = True
for curr in range(1, len(names)):
    prev = curr-1
    x,y = names[prev], names[curr]
    
    if not compare(x,y):
        flag = False
        break
    
# print("INCOMING:", incoming)
    
q = deque()
for order in range(ord('a'), ord('z')+1):
    if not flag: break
    char = chr(order)
    if incoming[char] == 0:
        q.append(char)
  
order = []
while q:
    if not flag: break
    
    char = q.popleft()
    order.append(char)
    
    for neighbor in graph[char]:
        incoming[neighbor] -= 1
        if incoming[neighbor] == 0:
            q.append(neighbor)
if not flag:
    print("Impossible")
elif len(order) == 26:
    print(''.join(order))
else:
    print("Impossible")
    
        
        
