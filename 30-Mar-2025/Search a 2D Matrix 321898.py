# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr):
            left, right = 0, len(arr)-1

            while left<=right:
                mid = (left+right)//2
                if arr[mid] == target:
                    return True

                if target<arr[mid]:
                    right = mid-1
                else:
                    left = mid+1

            return False

        for row in matrix:
            if binarySearch(row):
                return True

        return False