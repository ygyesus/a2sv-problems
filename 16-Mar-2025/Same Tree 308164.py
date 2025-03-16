# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def updateArr(node,arr):
            if not node:
                return

            
            arr.append(node.val)
            updateArr(node.left, arr)
            arr.append('L')
            updateArr(node.right, arr)
            arr.append('R')


        p_arr = []
        q_arr = []

        updateArr(p,p_arr)
        updateArr(q,q_arr)
        # print(p_arr)
        # print(q_arr)

        return p_arr == q_arr
        