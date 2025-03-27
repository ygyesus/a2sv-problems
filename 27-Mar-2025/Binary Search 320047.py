# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)  
        def binarySearch(left, right, target):
            
            if left<=right:
                mid = (left+right)//2

                if nums[mid] == target:
                    return mid

                if target>nums[mid]:
                    return binarySearch(mid+1, right, target)

                if target<nums[mid]:
                    return binarySearch(left, mid-1, target)

            return -1

        return binarySearch(0, n-1, target)
            
            
            