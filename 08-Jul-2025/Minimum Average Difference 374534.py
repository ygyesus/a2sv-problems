# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix = [0]
        n = len(nums)

        minDiff = float('inf')
        index = None

        for i in range(len(nums)):
            total = prefix[-1] + nums[i]
            prefix.append(total)

        for i in range(len(nums)):
            
            leftSum = prefix[i+1]
            left = i+1

            rightSum = prefix[-1] - prefix[i+1]
            right = n-i-1

            if not right:
                rightAvg = 0
            else:
                rightAvg = rightSum//right

            leftAvg = leftSum//left

            diff = abs(leftAvg - rightAvg)

            if diff<minDiff:
                minDiff = diff
                index = i

        return index

