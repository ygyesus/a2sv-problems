# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        
        
        current = root

        node = TreeNode(val)

        if not current:
            return node
        while True:
            if node.val<current.val:
                if not current.left:
                    current.left = node
                    return root
                else:
                    current = current.left

            elif node.val>current.val:
                if not current.right:
                    current.right = node
                    return root
                else:
                    current = current.right

            
