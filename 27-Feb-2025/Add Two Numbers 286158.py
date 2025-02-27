# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def sumOfList(head):
            current = head
            tenPower = 0

            ans = 0

            while current:
                num = current.val

                ans += num*10**tenPower
                tenPower += 1

                current = current.next

            return ans

        num = sumOfList(l1) + sumOfList(l2)

        dummy = ListNode()

        prev = dummy
        if not num:
            prev.next = ListNode(num)
            return dummy.next
        while num:
            digit = num%10

            node = ListNode(digit)
            prev.next = node

            prev = node

            num//=10

        return dummy.next




