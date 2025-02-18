# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1

        prefix = []

        for num in nums:
            product *= num
            prefix.append(product)

        suffix = []


        product = 1
        for num in nums[::-1]:
            product *= num
            suffix.append(product)

        suffix = suffix[::-1]

        # print("PREFIX:")
        # print(prefix)

        # print("SUFFIX:")
        # print(suffix)

        ans = []


        for i in range(len(nums)):
            if i>0:
                left = prefix[i-1]
            else:
                left = 1

            if i+1 >= len(nums):
                right = 1
            else:
                right = suffix[i+1]

            ans.append(right*left)

        return ans

        # print("ANS:")
        # print(ans)

            