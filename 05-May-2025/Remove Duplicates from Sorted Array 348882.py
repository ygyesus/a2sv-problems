# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1

        for right in range(len(nums)):
            if right>=1:
                if nums[right] != nums[right-1]:
                    nums[left] = nums[right]
                    left += 1

        for j in range(1,len(nums)):
            i = j-1

            if nums[j] <= nums[i]:
                return j
