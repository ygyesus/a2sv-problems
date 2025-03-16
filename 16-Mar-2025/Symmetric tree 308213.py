# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        def func1(node):
            if not node:
                return

            func1(node.left)
            arr1.append('L')

            arr1.append(node.val)

            func1(node.right)
            arr1.append('R')

        def func2(node):
            if not node:
                return
            func2(node.right)
            arr2.append('R')

            arr2.append(node.val)

            func2(node.left)
            arr2.append('L')

        func1(root)
        func2(root)

        # print(arr1)
        # print(arr2)

        if len(arr1) != len(arr2):
            return False

        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                if not [arr1[i], arr2[i]] in [['L','R'], ['R','L']]:
                    return False

        return True

        
