# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeroes = i = 0
        while i<len(arr):
            if arr[i] == 0:
                arr.pop()

                arr.insert(i+1, 0)

                i+=2
            else:
                i+=1

