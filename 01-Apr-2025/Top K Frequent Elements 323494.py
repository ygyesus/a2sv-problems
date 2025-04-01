# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        listOfChars = [(freq[char], char) for char in freq]

        
        def merge(leftSorted, rightSorted):
            i=j=0
            arr = []
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
                return [listOfChars[left]]

            mid = (left+right)//2

            leftSorted = mergeSort(left, mid)
            rightSorted = mergeSort(mid+1, right)

            return merge(leftSorted, rightSorted)


        n = len(listOfChars)
        
        ans = mergeSort(0, n-1)
        
        print(ans)
        res = []

        while k:
            x = ans.pop()[1]
            res.append(x)
            k-=1

        return res

            

        