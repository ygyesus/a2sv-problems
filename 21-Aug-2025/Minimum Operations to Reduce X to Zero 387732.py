# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        leftSums = dict()
        rightSums = dict()
        ans = float('inf')
        total = sum(nums)

        leftSum = 0
        for i in range(len(nums)):
            leftSum += nums[i]
            if leftSum == x: 
                ans = min(ans, i+1)
            leftSums[leftSum] = i+1
        rightSum = 0
        for j in range(len(nums)-1, -1, -1):
            rightSum += nums[j]
            if rightSum == x: 
                ans = min(ans, len(nums)-1 - j + 1)
            rightSums[rightSum] = len(nums)-1 - j + 1

            if x-rightSum in leftSums and not x>total:
                leftSum = x-rightSum
                ans = min(ans, rightSums[rightSum] + leftSums[leftSum])

        if not ans<float('inf'): return -1
        return ans
