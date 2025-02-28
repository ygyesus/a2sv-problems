# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

from collections import Counter, defaultdict
def getArray(LIST): return list(map(int, LIST))
# getArray(getSplit())

def getSplit(): return input().split()
def getInteger(): return int(input())


def getCheckpoints(a):
    zeroes = ones = 0
    
    checkpoints = []
    a = getArray(list(a))
#     print('a:', a)
    
    for i,num in enumerate(a):
        if num:
            ones += 1
        else:
            zeroes += 1
            
        if zeroes==ones:
            checkpoints.append(i)
            
    return checkpoints

t = int(input())
 
for _ in range(t):
    
#     print()
#     print("========================")
#     print("TEST CASE:", _)
    n = int(input())
     
    a = getArray(list(input()))
    b = getArray(list(input()))
    if a==b:
        print("YES")
        continue
    x = 0
    
    checkpoints = getCheckpoints(a)
#     print("CHECKPOINTS:", checkpoints)
    flag = True
#     print("=============================")
    if not checkpoints:
        flag = False
    for index, rightCheckpoint in enumerate(checkpoints):
        x = rightCheckpoint
        if not flag:
            break
        leftCheckpoint = 0 if index==0 else checkpoints[index-1]+1
        a_x = set()
        a_y = set()
        
        b_x = set()
        b_y = set()
        
        for checkpoint in range(leftCheckpoint, rightCheckpoint+1):

#             print("checkpoint:", checkpoint, a[checkpoint])
            if a[checkpoint] == 0:
                a_x.add(checkpoint)
            elif a[checkpoint] == 1:
                a_y.add(checkpoint)
                
            if b[checkpoint] == 0:
                b_x.add(checkpoint)
            elif b[checkpoint] == 1:
                b_y.add(checkpoint)


#         print('a_x == b_x :', a_x==b_x)
#         print('a_x == b_y :', a_x == b_y)
#         print("a_x:", a_x)
#         print("a_y:",a_y)
#         print("b_x:",b_x)
#         print("b_y:",b_y)
#         print("________________")
        if not (a_x == b_x or a_x == b_y):
            flag = False
            break
            
        if not flag:
            break
        
    for i in range(x+1, n):
        if a[i] != b[i]:
            flag = False
            break
        
    if flag:
        print("YES")
    else:
        print("NO")
                

