# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Negative = 0, add positives tho

        
        positiveTotal = maxPositiveTotal = negativeTotal = minNegativeTotal = 0

        for num in nums:
            positiveTotal += num
            negativeTotal += num

            if positiveTotal < 0:
                positiveTotal = 0

            if negativeTotal > 0:
                negativeTotal = 0

            maxPositiveTotal = max(maxPositiveTotal, positiveTotal)
            minNegativeTotal = min(minNegativeTotal, negativeTotal)

        # print(maxPositiveTotal, -minNegativeTotal)
        return max(maxPositiveTotal, -minNegativeTotal)
