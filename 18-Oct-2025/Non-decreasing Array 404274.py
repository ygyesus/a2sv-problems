# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        maxChanges = 1
        # check i-1 / i-1 should be decreased
        def checkLess(i):
            if i-1 == 0: 
                nums[i-1] = float('-inf')
                return True
            if nums[i-2] <= nums[i]:
                nums[i-1] = nums[i-2]
                return True
            return False

        # check i / i should be increased
        def checkMore(i):
            if i==n-1:
                nums[i] = float('inf')
                return True
            
            if nums[i-1] <= nums[i+1]:
                nums[i] = nums[i-1]
                return True

            return False


        

        n = len(nums)
        maxChanges = 1
        
        for i in range(1, n):
            if not nums[i-1] <= nums[i]:
                if not maxChanges: return False
                if checkLess(i) or checkMore(i):
                    maxChanges -= 1

        return nums==sorted(nums)
               