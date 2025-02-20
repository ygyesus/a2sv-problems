# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.dummy = ListNode()
        self.dummy.next = head

        # visited = set()

        current = head

        prev = self.dummy
        while current and current.next:
            if current.val == current.next.val:
                prev.next = current.next
            else:
                prev = current
                # visited.add(current.val)
                
            current = current.next

        return self.dummy.next