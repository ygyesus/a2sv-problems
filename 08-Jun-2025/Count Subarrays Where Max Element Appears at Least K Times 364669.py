# Problem: Count Subarrays Where Max Element Appears at Least K Times - https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)

        n = len(nums)
        count = 0

        left = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == maxNum:
                count += 1

            while count >= k:
                if nums[left] == maxNum:
                    count -= 1
                left += 1

                ans += n-right

        return ans