# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = Counter()

        total = maxTotal = 0
        left = 0

        for right in range(k):
            total += nums[right]
            freq[nums[right]] += 1

        if len(freq) == k:
            maxTotal = max(maxTotal, total)

        for right in range(k, len(nums)):

            total -= nums[left]
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1

            total += nums[right]
            freq[nums[right]] += 1

            if len(freq) == k:
                maxTotal = max(maxTotal, total)

        return maxTotal
