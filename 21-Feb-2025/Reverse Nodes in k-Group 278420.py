# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        array = []

        current = head

        while current:
            array.append(current.val)
            current = current.next

        i=0
        while i+k<=len(array):
            array[i:i+k] = array[i:i+k][::-1]
            i+=k

        dummy = ListNode()

        dummy.next = head
        current = dummy.next
        for num in array:
            current.val = num
            current = current.next

        return dummy.next