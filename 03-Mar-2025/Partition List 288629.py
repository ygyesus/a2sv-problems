# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftDummy = ListNode()
        rightDummy = ListNode()

        leftLast = leftDummy
        rightDummy.next = head

        current = rightDummy

        while current and current.next:
            if current.next.val < x:
                leftLast.next = current.next
                leftLast = leftLast.next
                current.next = current.next.next
            else:
                current = current.next

        leftLast.next = rightDummy.next

        return leftDummy.next