# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        
        def check(radius):
            # two pointers

            house, heater = 0,0
            while house<len(houses) and heater<len(heaters):
                if abs(houses[house] - heaters[heater]) > radius:
                    heater += 1

                else:
                    house += 1

            return house >= len(houses)

        heaters.sort()
        houses.sort()
        
        left,right = 0,10**9

        ans = float('inf')
        while left<=right:

            radius = (left+right)//2

            if check(radius):
                ans = min(ans, radius)
                right = radius - 1
            else:
                left = radius + 1

        return ans