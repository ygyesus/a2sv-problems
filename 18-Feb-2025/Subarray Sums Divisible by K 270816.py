# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total = 0

        freq = defaultdict(int)
        freq[0] = 1
        ans = 0
        for i in range(len(nums)):
            total += nums[i]
            
            if total%k in freq:
                ans += freq[total%k]
            freq[total%k] += 1

        return ans