# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = [(root, 0)]

        mapping = defaultdict(list)
        while q:
            node, level = q.pop(0)
            mapping[level].append(node)
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))

        mapping = dict(mapping)

        for level in mapping:
            if level%2 == 1:
                mapping[level] = mapping[level][::-1]

        stack = [root]
        for level in range(1, len(mapping)):
            parents = mapping[level-1]
            childIndex = 0
            children = mapping[level]

            while childIndex<len(children):
                LEFT = children[childIndex]
                RIGHT = children[childIndex+1]
                parentIndex = childIndex//2

                parents[parentIndex].left = LEFT
                parents[parentIndex].right = RIGHT

                childIndex += 2

            
        return root
