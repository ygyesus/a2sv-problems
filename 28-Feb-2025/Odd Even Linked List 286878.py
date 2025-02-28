# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        oddDummy = ListNode()
        evenDummy = ListNode()

        oddDummy.next = head

        oddPrev = oddDummy
        evenPrev = evenDummy

        i = 1

        current = head

        while current:
            if i%2:
                oddPrev.next = current
                oddPrev = current
                evenPrev.next = current.next

            else:
                evenPrev.next = current
                evenPrev = current

                oddPrev.next = current.next

            i += 1
            current = current.next

        print(oddDummy)
        print(evenDummy)

        oddPrev.next = evenDummy.next

        return oddDummy.next


