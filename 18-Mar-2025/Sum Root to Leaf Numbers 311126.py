# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [(root, str(root.val))]

        total = 0
        while stack:
            node, numString = stack.pop()

            if (not node.left and not node.right):
                total += int(numString)
            else:
                if node.left:
                    duo = (node.left, numString + str(node.left.val))
                    stack.append(duo)
                if node.right:
                    duo = (node.right, numString + str(node.right.val))
                    stack.append(duo)

        return total