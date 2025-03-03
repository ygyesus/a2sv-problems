# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total1 = total2 = 0

        curr1 = l1
        curr2 = l2

        while curr1:
            total1 = 10*total1 + curr1.val
            curr1 = curr1.next

        while curr2:
            total2 = 10*total2 + curr2.val
            curr2 = curr2.next

        total = total2 + total1

        total = str(total)

        prev = dummy = ListNode()

        for digit in total:
            prev.next = ListNode(int(digit))
            prev = prev.next

        return dummy.next