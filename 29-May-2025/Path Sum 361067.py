# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root: return False

        def dfs(node, total):

            total += node.val

            if not (node.left or node.right):
                return total == targetSum

            ans = False

            if node.left:
                ans = ans or dfs(node.left, total)
            if node.right:
                ans = ans or dfs(node.right, total)
            return ans

        return dfs(root, 0)