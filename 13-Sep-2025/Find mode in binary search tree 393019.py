# Problem: Find mode in binary search tree - https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = Counter()

        def dfs(node):
            if not node: return
            counter[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        if counter: maxFreq = max(counter.values())

        ans = []
        for num in counter:
            if counter[num] == maxFreq:
                ans.append(num)

        return ans

        
        