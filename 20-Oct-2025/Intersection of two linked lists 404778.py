# Problem: Intersection of two linked lists - https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr = headA
        visited = set()

        while curr:
            visited.add(curr)
            curr = curr.next

        curr = headB
        while curr:
            if curr in visited: break
            curr = curr.next

        return curr