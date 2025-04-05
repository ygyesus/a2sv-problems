# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        left = max(nums)
        right = sum(nums)

        def check(total):
            
            sumTotal = 0

            arrays = 0
            for i in range(len(nums)):
                if sumTotal + nums[i] > total:
                    sumTotal = nums[i]
                    arrays += 1
                    
                else:
                    sumTotal += nums[i]

            arrays += 1

            return arrays <= k


        ans = None
        while left<=right:
            mid = (left+right)//2

            if check(mid):
                ans = mid
                right = mid-1

            else:
                left = mid+1

        return ans


            