# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        

        n = len(nums)
        left, right = 0, n-1
        while left<right:
            while left<right and nums[left] != val:
                left += 1

            # LEFT 
            while left<right and nums[right] == val:
                right -= 1

            if left<right:
                nums[left], nums[right] = nums[right], nums[left]

        while nums and nums[-1] == val: nums.pop()
        return len(nums)


