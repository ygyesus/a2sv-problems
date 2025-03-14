# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        count = 1
        maxCount = [1]
        def depth(node, count):
            if not node:
                return

            maxCount[0] = max(maxCount[0], count)
            max
            if node.left:
                depth(node.left, count+1)
            if node.right:
                depth(node.right, count+1)

        depth(root, count)
        print(maxCount)
        return maxCount.pop()
            