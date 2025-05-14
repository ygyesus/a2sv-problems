# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        powerSet = []

        for mask in range(1<<len(nums)):
            arr = list()
            for i in range(len(nums)):
                if mask>>i & 1:
                    arr.append(nums[i])

            powerSet.append(arr)
        return powerSet
            