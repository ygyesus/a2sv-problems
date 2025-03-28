# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()
        def check(time, cars):

            for rank in ranks:
                cars -= (time/rank)**0.5
                cars = ceil(cars)

            return not cars>0

        left, right = 0, (ranks[0]*cars**2)
        while left<=right:
            mid = (left+right)//2

            if check(mid, cars):
                right = mid-1
            else:
                left = mid+1

        return left

            