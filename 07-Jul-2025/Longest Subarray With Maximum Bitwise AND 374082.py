# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = max(nums)
        maxAns = float('-inf')
        left = 0
        while left < (len(nums)):
            right, ans = left, 0
            while nums[right] == k:
                ans += 1
                right += 1
                left += 1
                if right==len(nums): break


            maxAns = max(maxAns, ans)
            left += 1

        return maxAns