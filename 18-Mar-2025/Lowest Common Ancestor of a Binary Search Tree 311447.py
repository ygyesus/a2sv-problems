# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        myDict = dict()
        def findVisited(node, level):
            if not node:
                return set()

            visitedDescendants = findVisited(node.left, level+1).union(findVisited(node.right, level+1))

            visitedDescendants.add(node)

            if p in visitedDescendants and q in visitedDescendants:
                myDict[node] = visitedDescendants, level
            

            return visitedDescendants


        level = 0
        findVisited(root, level)

        maxNode = root
        for node in myDict:
            if myDict[node][-1] > myDict[maxNode][-1]:
                maxNode = node

        return maxNode
        



        