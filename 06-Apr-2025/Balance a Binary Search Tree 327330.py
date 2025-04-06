# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        array = []

        def dfs(node):
            if not node:
                return

            array.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        array.sort()

        def helper(left, right):

            if not left<=right:
                return None

            mid = (left+right)//2

            root = TreeNode(array[mid])
            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)

            return root

        n = len(array)

        return helper(0,n-1)

        