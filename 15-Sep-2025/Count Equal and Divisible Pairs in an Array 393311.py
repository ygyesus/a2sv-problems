# Problem: Count Equal and Divisible Pairs in an Array - https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = 0

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    if (i*j)%k == 0:
                        pairs += 1

        return pairs