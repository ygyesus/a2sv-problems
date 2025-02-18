# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        
        ans = []

        # PREFIX
        for i in range(len(nums)):
            ans.append(product)
            product *= nums[i]


        # SUFFIX
        product = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= product

            product *= nums[i]


        return ans

        