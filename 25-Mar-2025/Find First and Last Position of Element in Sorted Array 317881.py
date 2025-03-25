# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        ans = [-1, -1]

        left, right = 0, len(nums)-1

        # start
        while left<=right:
            mid = (left+right)//2

            if nums[mid] >= target:
                if nums[mid] == target:
                    ans[0] = mid

                right = mid - 1

            else:
                left = mid+1

        left, right = 0, len(nums)-1
        # end
        while left<=right:
            mid = (left+right)//2

            if nums[mid] <= target:
                if nums[mid] == target:
                    ans[1] = mid

                left = mid + 1

            else:
                right = mid-1

        return ans



