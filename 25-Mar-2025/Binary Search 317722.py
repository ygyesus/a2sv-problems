# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(target):
            left = 0
            right = len(nums)-1

            mid = (left+right)//2

            while left < right and nums[mid] != target:

                if target<nums[mid]:
                    right = mid-1
                else:
                    left = mid + 1

                mid = (left+right)//2

            if nums[mid] == target:
                return mid
            
            return -1

        return binarySearch(target)
