# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]

        ans = []
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
            if node and node.right:
                stack.append(node.right)
            if node and node.left:
                stack.append(node.left)


        # print(ans)
        return ans
