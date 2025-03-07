# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)

        keys = freq.keys()
        keys = sorted(list(keys), key = lambda key: -freq[key])

        totalCount = 0
        for i,key in enumerate(keys):
            totalCount += freq[key]

            if totalCount >= len(arr)/2:
                return i+1

