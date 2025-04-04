# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        arr = []

        current = head

        while current:
            arr.append(current.val)
            current = current.next

        arr.sort()

        dummy = ListNode()

        prev = dummy
        for i in range(len(arr)):
            prev.next = ListNode(arr[i])
            prev = prev.next

        return dummy.next