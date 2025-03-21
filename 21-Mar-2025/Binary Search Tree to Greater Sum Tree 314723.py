# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        setOfNums = set()
        def dfs(node):
            if not node:
                return

            setOfNums.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        listOfNums = sorted(setOfNums, key = lambda x: -x)

        # print("listOfNums:", listOfNums)
        greaterMap = {}
        greater = 0

        for num in listOfNums:
            greater += num
            greaterMap[num] = greater

        # print(greaterMap)

        def dfs(node):
            if not node:
                return
            
            node.val = greaterMap[node.val]
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return root

        

        

        

