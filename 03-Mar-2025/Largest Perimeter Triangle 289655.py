# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        def isValid(x,y,z):
            if not x+y > z:
                return False

            if not x+z > y:
                return False

            if not y+z > x:
                return False

            return True

        nums.sort()

        x,y,z = len(nums)-3, len(nums)-2, len(nums)-1
        total = 0

        while not isValid (nums[x], nums[y], nums[z]):
            x-=1
            y-=1
            z-=1

            if not x>=0:
                return 0

        return nums[x] + nums[y] + nums[z]