# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

from collections import defaultdict

n = int(input())

class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val
        self.children = []
root = TreeNode(1)
count = 1
numToNode = {
    1: root
}

def recur(node):
    if not node.children:
        return True
    
    leafChildren = 0
    for child in node.children:
        if not child.children:
            leafChildren += 1
            
    if not leafChildren >= 3:
        return False
        
    for child in node.children:
        if not recur(child):
            return False
        
    return True
    


for _ in range(n-1):
    parent = int(input())
    count += 1
    
    parentTree = numToNode[parent]
    child = TreeNode(count)
    numToNode[count] = child
    parentTree.children.append(child)
    
    

if recur(root):
    print("Yes")
else:
    print("No")
    
    
    
    
    
    
