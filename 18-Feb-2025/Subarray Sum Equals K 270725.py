# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        freq = defaultdict(int)
        freq[0] += 1

        total = 0
        ans = 0
        
        for num in nums:
            total += num            
            if total-k in freq:
                ans += freq[total-k]
            freq[total] += 1

        return ans