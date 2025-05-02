# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        
        heap = []
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                x = grid[row][col] = (-grid[row][col], row)
                heap.append(x)


        heapify(heap)

        total = 0
        while k:
            member, row = heappop(heap)

            if not limits[row]: continue
            total += member
            limits[row] -= 1
            k -= 1

        return -total
