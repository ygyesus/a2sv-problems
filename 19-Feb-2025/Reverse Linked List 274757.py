# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        current = head

        while current:
            stack.append(current.val)
            current = current.next

        dummy = ListNode()
        current = dummy
        while stack:
            val = stack.pop()

            node = ListNode(val)
            current.next = node
            current = node

        return dummy.next

            


