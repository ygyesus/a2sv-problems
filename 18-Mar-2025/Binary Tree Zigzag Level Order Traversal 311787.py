# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        row1 = [root]
        row2 = []

        traversed = [[root]]
        count = 0
        while row1:

            for parent in row1:
                if parent:
                    if parent.left:
                        row2.append(parent.left)
                    if parent.right:
                        row2.append(parent.right)

            if row2:
                traversed.append(row2[::-1]) if count%2 == 0 else traversed.append(row2)
            count += 1

            # print("row2:", row2)
            # print("traversed:", traversed)
            row1 = row2
            row2 = []



        # print("TRAVERSED:", traversed)
        # for member in traversed:
        #     print("MEMBER:", member)
        #     print("================")

    
        for LIST in traversed:
            # if LIST == [None]:
            #     continue

            # print("LIST:", LIST)
            for i,node in enumerate(LIST):
                if node:
                    LIST[i] = node.val
            # print("LENGTH:", len(LIST))

        # print(traversed)
        return traversed
        


    
