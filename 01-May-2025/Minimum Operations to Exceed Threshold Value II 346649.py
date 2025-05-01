# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = 0

        heapify(nums)

        while len(nums) >=2 and nums[0] < k:
            x,y = heappop(nums), heappop(nums)
            new = (min(x, y) * 2 + max(x, y)) 
            heappush(nums, new)
            ops += 1

        return ops