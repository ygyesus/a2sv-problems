# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n not in nums:
            return n

        for i in range(len(nums)):
            
            while nums[i] != n:
                correct = nums[i]

                if nums[i] == nums[correct]:
                    break

                nums[i], nums[correct] = nums[correct], nums[i]

        for i in range(len(nums)):
            if i!=nums[i]:
                return i

            