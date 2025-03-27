# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        mapping = {}

        for i in range(len(arr)):
            mapping[i] = arr[i]

        i = 0

        
        for value in mapping.values():
            if i>=len(arr):
                break
            arr[i] = value
            i+=1

            if i>=len(arr):
                break
                
            if value == 0:
                arr[i] = value
                i+=1

