# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        freq = Counter()
        pairs = ans = 0
        left = 0
        for right in range(len(nums)):
            freq[nums[right]] += 1

            pairs += (freq[nums[right]]-1)

            while pairs >= k:
                pairs -= (freq[nums[left]]-1)
                freq[nums[left]] -= 1
                left += 1

            lastLeft = left-1
            ans += lastLeft+1

        return ans

            