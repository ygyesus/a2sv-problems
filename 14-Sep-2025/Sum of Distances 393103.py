# Problem: Sum of Distances - https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        def binarySearch(valueIndices, i):
            left, right = 0, len(valueIndices)-1

            while left<=right:
                mid = (left+right)//2
                if i==valueIndices[mid]:
                    return mid
                elif i<valueIndices[mid]:
                    right = mid-1
                elif i>valueIndices[mid]:
                    left = mid+1
                

        n = len(nums)
        arr = [0] * n

        valueToIndices = defaultdict(list)

        for i, value in enumerate(nums):
            valueToIndices[value].append(i)

        prefixes = {}
        for value in valueToIndices:
            if len(valueToIndices[value]) == 1: continue
            prefix = [valueToIndices[value][0]]
            for curr in range(1, len(valueToIndices[value])):
                total = prefix[-1] + valueToIndices[value][curr]
                prefix.append(total)

            prefixes[value] = prefix

        for i, value in enumerate(nums):
            if len(valueToIndices[value]) == 1: continue
            valueIndices = valueToIndices[value]
            mid = binarySearch(valueIndices, i)
            prevTotal = 0
            nextTotal = 0
            prefix = prefixes[value]
            if mid>0:
                prevTotal = prefix[mid] - i
            if mid<len(prefix)-1:
                nextTotal = prefix[-1] - prefix[mid]

            prevMembers = mid
            nextMembers = len(valueIndices) - (prevMembers+1)
            ans = (i*prevMembers - prevTotal) + (nextTotal - i*nextMembers)
            arr[i] = ans

        return arr
            
            




        

