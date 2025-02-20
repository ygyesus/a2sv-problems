# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        
        distance = 0
        dummy.next = head

        fast = head

        while fast and fast.next:
            fast = fast.next.next
            distance += 2

        if not fast:
            distance -= 1

        current = dummy

        count = 0
        while count<distance-(n-1):
            current = current.next
            count += 1

        print(current.val)
        current.next = current.next.next
        return dummy.next