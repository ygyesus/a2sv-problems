# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        maxValue = minValue = root.val
        def func(node, maxValue, minValue):
            if not node:
                maxDiff = maxValue - minValue
                return maxDiff

            maxValue = max(maxValue, node.val)
            minValue = min(minValue, node.val)
            maxDiff = maxValue - minValue
            return max(maxDiff, func(node.left, maxValue, minValue), func(node.right, maxValue, minValue))

        return func(root, maxValue, minValue)

