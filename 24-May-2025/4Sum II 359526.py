# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        n = len(nums1)

        counter = Counter()

        for i in range(n):
            for j in range(n):
                total = nums1[i] + nums2[j]
                counter[total] += 1
        ans = 0
        for k in range(n):
            for l in range(n):
                total = nums3[k] + nums4[l]
                ans += counter[-total]

        return ans
        