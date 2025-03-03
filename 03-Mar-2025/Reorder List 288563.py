# Problem: Reorder List - https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            prev = None
            current = head

            while current:
                nextNode = current.next
                current.next = prev

                prev = current
                current = nextNode

            return prev

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current2 = reverse(slow)

        current1 = head

        flag = True
        dummy = ListNode()
        prev = dummy

        while current1 != current2:
            if flag:
                prev.next = current1
                prev = current1
                current1 = current1.next
                flag = False
            else:
                prev.next = current2
                prev = current2
                current2 = current2.next
                flag = True