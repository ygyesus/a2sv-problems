# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def binarySearch(left, right):

            while left<=right:

                mid = (left+right)//2

                # part of left
                if nums[mid] >= nums[0]:
                    left = mid+1
                # part of right
                else:
                    if nums[mid-1] > nums[mid]:
                        return nums[mid]

                    right = mid-1

            return nums[0]

        return binarySearch(0, len(nums)-1)