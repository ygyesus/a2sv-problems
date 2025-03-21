# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        ans = {'key': 0}
        
        def dfs(node):
            if not node:
                return {
                    'total': 0,
                    'count': 0
                }


            dictLeft = dfs(node.left)
            dictRight = dfs(node.right)

            # print(node.val, dictLeft, dictRight)
            myDict = {
                'total': node.val + dictLeft['total'] + dictRight['total'],
                'count': 1 + dictLeft['count'] + dictRight['count']
            }

            total, count = myDict['total'], myDict['count']

            if total//count == node.val:
                ans['key'] += 1

            # print(node.val, myDict)
            return myDict

        dfs(root)
        return ans['key']
        
        