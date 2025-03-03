# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # prev.next = curr.next
    # curr.next.next = curr
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        first = head

        while first and first.next:
            second = first.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            first = first.next

        # print(head)
        return dummy.next