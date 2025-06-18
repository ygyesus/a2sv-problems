# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):

                ans += gcd(*nums[i:j+1])==k

        return ans