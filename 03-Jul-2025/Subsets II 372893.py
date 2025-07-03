# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        for mask in range(1<<len(nums)):

            move = 0
            TUPLE = ()
            while mask>>move:
                if mask>>move & 1:
                    TUPLE += (nums[move],)
                move += 1

            ans.add(tuple(sorted(list(TUPLE))))

        ans = [sorted(list(x)) for x in ans]
        ans.sort()
        return ans