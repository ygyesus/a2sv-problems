# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def dfs(node):
            if not node: return 0

            maxAns = 0
            for child in node.children:
                ans = dfs(child)
                maxAns = max(maxAns, ans)

            return 1+maxAns

        return dfs(root)

        


        