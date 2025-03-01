# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack = []


        current = head

        while current:
            stack.append(current.val)
            current = current.next

        head = ListNode()

        left -= 1
        right -= 1

        dummy = ListNode()
        prev = dummy
        while left<right:
            stack[left], stack[right] = stack[right], stack[left]
            left += 1
            right -= 1

        for val in stack:
            prev.next = ListNode(val)
            prev = prev.next

        return dummy.next

        