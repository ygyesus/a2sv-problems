# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(leftSorted, rightSorted):
            arr = []

            i = j = 0

            while i<len(leftSorted) and j<len(rightSorted):
                if leftSorted[i] <= rightSorted[j]:
                    arr.append(leftSorted[i])
                    i+=1
                else:
                    arr.append(rightSorted[j])
                    j+=1

            while i<len(leftSorted):
                arr.append(leftSorted[i])
                i+=1

            while j<len(rightSorted):
                arr.append(rightSorted[j])
                j+=1

            return arr

        def mergeSort(left, right):
            if left==right:
                return [nums[left]]

            mid = (left+right)//2

            leftSorted = mergeSort(left, mid)
            rightSorted = mergeSort(mid+1, right)

            return merge(leftSorted, rightSorted)

        return mergeSort(0, len(nums)-1)

            