# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        valueToIndex = {}

        for i, value in enumerate(nums):
            valueToIndex[value] = i

        for prevValue, newValue in operations:
            prevIndex = valueToIndex[prevValue]
            nums[prevIndex] = newValue
            valueToIndex[newValue] = prevIndex

        return nums