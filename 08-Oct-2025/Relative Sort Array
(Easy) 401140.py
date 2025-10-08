# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # All elements in arr2 are also in arr1


        arr1_Elements = Counter(arr1)

        arr2_Elements = Counter(arr2)
        ans = []



        for num in arr2:
            while arr1_Elements[num] > 0:
                ans.append(num)
                arr1_Elements[num] -= 1


        appended = []
        for num in arr1:
            if num not in arr2_Elements:
                appended.append(num)

        appended.sort()

    
        ans.extend(appended)
        return ans


