# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head

        slow = head
    
        count = 0

        while True:
            if fast.next:
                fast = fast.next
                count += 1
                slow = slow.next
                if fast.next:
                    fast = fast.next
                    count += 1
                else:
                    break

            else:
                break

        destination = count//2

        count //= 2

        print(count, destination)

        while count<destination:
            slow = slow.next
            count += 1

        return slow
        
