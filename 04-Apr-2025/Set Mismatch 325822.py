# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            correct = nums[i]-1

            while nums[correct] != nums[i]:
                nums[i], nums[correct] = nums[correct], nums[i]
                correct = nums[i]-1

        for i in range(len(nums)):
            if nums[i]-1 != i:
                return [nums[i], i+1]