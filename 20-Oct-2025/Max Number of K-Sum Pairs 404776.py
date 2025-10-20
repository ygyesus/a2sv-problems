# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        ans = 0
        for num in nums:
            if num > k//2: continue
            if not num in counter: continue
            if k-num == num:
                ans += counter[num]//2
                del counter[num]
            else:
                ans += min(counter[num], counter[k-num])
                del counter[num]
                del counter[k-num]

        return ans
