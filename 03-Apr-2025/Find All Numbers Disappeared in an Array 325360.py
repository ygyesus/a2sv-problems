# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            correct = nums[i]-1
            while nums[correct] != nums[i]:
                nums[i], nums[correct] = nums[correct], nums[i]
                correct = nums[i]-1


        for i in range(len(nums)):
            if i!=nums[i]-1:
                ans.append(i+1)

        return ans