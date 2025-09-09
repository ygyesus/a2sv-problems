# Problem: Left-and-right-sum-differences - https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        def helper(nums):
            leftSum = []
            leftTotal = 0

            for i in range(len(nums)):
                leftSum.append(leftTotal)
                leftTotal += nums[i]

            return leftSum

        leftSum = helper(nums)
        rightSum = helper(nums[::-1])[::-1]
        ans = []

        for i in range(len(leftSum)):
            left, right = leftSum[i], rightSum[i]
            diff = abs(left-right)
            ans.append(diff)

        return ans