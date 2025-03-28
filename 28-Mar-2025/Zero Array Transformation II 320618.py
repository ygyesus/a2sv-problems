# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if nums == [0]*len(nums):
            return 0
        def check(k, nums):
            prefix = [0] * len(nums)
            for l, r, val in queries[:k]:
                prefix[l] -= val
                if r+1 < len(nums):
                    prefix[r+1] += val

            for i in range(1, len(prefix)):
                prefix[i] += prefix[i-1]

            for i in range(len(nums)):
                nums[i] += prefix[i]
                if nums[i] < 0:
                    nums[i] = 0

            # print(nums)

            return nums == [0] * len(nums)
            
        left, right = 1, len(queries)
        ans = -1
        while left<=right:
            k = (left+right)//2

            copy = [x for x in nums]
            if check(k, copy):
                right = k-1
                ans = k
            else:
                left = k+1

        return ans
        