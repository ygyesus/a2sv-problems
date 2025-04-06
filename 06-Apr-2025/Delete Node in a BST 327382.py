# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root

        stack = [root]
        arr = []

        def dfs():

            while stack:
                node = stack.pop()
                arr.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        dfs()
        
        arr.sort()
        if key in arr:
            arr.remove(key)

        def helper(left, right):
            if not left<=right:
                return None

            mid = (left+right)//2
            root = TreeNode(arr[mid])

            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)
            return root

        n = len(arr)

        return helper(0, n-1)