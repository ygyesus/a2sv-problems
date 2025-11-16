# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row, col = 0, 0
        curr = head
        i = 0
        
        # Initialize first cell
        grid[0][0] = head.val
        curr = curr.next
        
        while curr:
            new_row, new_col = row + directions[i % 4][0], col + directions[i % 4][1]
            
            if not (0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == -1):
                i += 1
                continue
            
            row, col = new_row, new_col
            grid[row][col] = curr.val
            curr = curr.next
        
        return grid