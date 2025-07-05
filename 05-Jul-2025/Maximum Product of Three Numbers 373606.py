# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        nums.sort()

        maxAns = float('-inf')
        if nums[0]<0 and nums[1]<0:
            ans = nums[0]*nums[1]*nums[-1]
            maxAns = max(maxAns, ans)

        product = 1
        for _ in range(3):
            product *= nums.pop()

        maxAns = max(maxAns, product)
        return maxAns