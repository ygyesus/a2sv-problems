# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        
        def backtrack(node, path):
            children = [node.left, node.right]
            if children == [None, None]:
                paths.append(path[:])
                return

            for child in children:
                if not child: continue
                path.append(str(child.val))
                backtrack(child, path)
                path.pop()

        backtrack(root, [str(root.val)])
        return (["->".join(path) for path in paths])
    

        

        


