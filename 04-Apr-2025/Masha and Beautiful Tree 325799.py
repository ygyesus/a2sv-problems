# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

t = int(input())

       
def merge(leftSorted, rightSorted, count):
    
    
    arr = sorted(leftSorted+rightSorted)
    if count == -1:
        return arr, count
    if not leftSorted+rightSorted == arr:
        count += 1
        if not rightSorted + leftSorted == arr:
            return arr, -1
        
    return arr, count
        
        
def mergeSort(left, right, count):
    if left==right:
        return [a[left]], 0
    
    mid = (left+right)//2
    
    leftSorted, countLeft = mergeSort(left, mid, 0)
    rightSorted, countRight = mergeSort(mid+1, right, 0)
    
    if -1 in [countLeft, countRight]:
        return merge(leftSorted, rightSorted, -1)
        
    
    return merge(leftSorted, rightSorted, count + countLeft + countRight)


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    arr, count = mergeSort(0, n-1, 0)
    print(count)
    