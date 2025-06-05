# Problem: Arithmetic Subarrays - https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArithmetic(arr):

            if not len(arr)>=2: return False

            new = sorted(arr)

            diff = new[1] - new[0]

            for j in range(1, len(arr)):
                if new[j] - new[j-1] != diff:
                    return False

            return True
        ans = []
        for i in range(len(l)):

            left, right = l[i], r[i]

            ans.append(isArithmetic(nums[left:right+1]))

        return ans
        