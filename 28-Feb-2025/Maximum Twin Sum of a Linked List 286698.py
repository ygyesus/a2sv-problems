# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        secondHalfDummy = ListNode()
        prev = None

        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode

        print(secondHalfDummy)
        parallel = prev

        current = head

        twinSum = maxTwinSum = 0

        while parallel:
            twinSum = current.val + parallel.val

            maxTwinSum = max(maxTwinSum, twinSum)
            current = current.next
            parallel = parallel.next

        return maxTwinSum


        
        

        