# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0

        count = 0

        maxLength = 0
        for right in range(len(nums)):
            count += 1-nums[right]

            while count>1:
                count -= 1-nums[left]
                left += 1

            length = right-left
            maxLength = max(maxLength, length)

        return maxLength