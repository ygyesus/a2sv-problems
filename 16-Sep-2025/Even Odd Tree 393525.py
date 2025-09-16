# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0

        while q:
            if not q[0].val%2==1-(level%2): return False
            if level%2==0:
                for i in range(1, len(q)):
                    if not (q[i].val%2==1-(level%2) and q[i].val>q[i-1].val):
                        return False

            else:
                for i in range(1, len(q)):
                    if not (q[i].val%2==1-(level%2) and q[i].val<q[i-1].val):
                        return False                

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return True



