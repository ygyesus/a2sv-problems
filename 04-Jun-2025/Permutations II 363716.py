# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        options = []
        def backtrack(indices):

            if len(indices) == len(nums):
                options.append(indices[:])
                return

            for i in range(len(nums)):
                if i in indices: continue
                indices.append(i)
                backtrack(indices)
                indices.pop()

        backtrack([])
        # print(options)
        ans = set()
        for indices in options:

            for i in range(len(indices)):
                numIndex = indices[i]
                indices[i] = nums[numIndex]

            ans.add(tuple(indices))

        ans = [list(TUPLE) for TUPLE in ans]
        return ans
        
        