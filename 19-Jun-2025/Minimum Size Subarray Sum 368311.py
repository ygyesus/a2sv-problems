# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target: return 0
        left = 0


        total = 0
        minAns = float('inf')
        for right in range(len(nums)): 
            total += nums[right]

            while total >= target:

                ans = right-left+1
                minAns = min(minAns, ans)

                total -= nums[left]
                left += 1

        return minAns
    