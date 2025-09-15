# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levelToList = {}
        def dfs(node, level):
            if not node: return
            if not level in levelToList: levelToList[level] = []
            levelToList[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root, 0)
        ans = [i for i in range(len(levelToList))]
        for level in range(len(levelToList)):
            ans[level] = sum(levelToList[level])/len(levelToList[level])

        return ans

