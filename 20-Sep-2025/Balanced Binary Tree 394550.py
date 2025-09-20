# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        BOOL = True
        def dfs(node):
            nonlocal BOOL
            if not node: return 0
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            if not abs(leftDepth-rightDepth) <= 1: BOOL = False
            return max(leftDepth, rightDepth) + 1

        dfs(root)
        return BOOL

        