# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans += nums[i]+nums[j]<target

        return ans