# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        maximumOfRow = defaultdict(int)
        stack = [(root, 1)]
        
        

        while stack:
            duo = stack.pop()
            node, row = duo

            if node.left:
                stack.append((node.left, row+1))
            if node.right:
                stack.append((node.right, row+1))

            if not row in maximumOfRow:
                maximumOfRow[row] = node.val
            else:
                maximumOfRow[row] = max(maximumOfRow[row], node.val)

        # print(dict(maximumOfRow))

        return list(maximumOfRow.values())

            

        