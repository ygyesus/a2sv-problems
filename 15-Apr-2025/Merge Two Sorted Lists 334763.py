# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        prev = dummy



        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next

            else:
                prev.next = list2
                prev = list2
                list2 = list2.next

        while list1:
            prev.next = list1
            prev = list1
            list1 = list1.next

        while list2:
            prev.next = list2
            prev = list2
            list2 = list2.next

        return dummy.next

