# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        rightHead = ListNode()
        leftHead = ListNode()
        leftLast = leftHead
        rightHead.next = head

        current = rightHead
        while current and current.next:

            if current.next.val < x:
                # update leftLast to current.next.next and skip current.next.next
                leftLast.next = current.next
                leftLast = current.next
                current.next = current.next.next
                # current = current.next
            else:
                current = current.next


        print("LEFTHEAD")
        current = leftHead.next
        while current:
            print(current.val)
            current = current.next
        print("================")
        print("RIGHTHEAD")
        current = rightHead.next

        while current:
            print(current.val)
            current = current.next
        leftLast.next = rightHead.next

        return leftHead.next