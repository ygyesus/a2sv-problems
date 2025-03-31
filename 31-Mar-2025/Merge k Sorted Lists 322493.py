# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        arr = []
        for LIST in lists:

            curr = LIST

            while curr:
                arr.append(curr.val)
                curr = curr.next

        arr.sort(key = lambda x: -x)

        dummy = ListNode()

        curr = dummy

        count = 0
        while arr:
            node = ListNode(arr.pop())
            curr.next = node
            curr = curr.next

        return dummy.next
            