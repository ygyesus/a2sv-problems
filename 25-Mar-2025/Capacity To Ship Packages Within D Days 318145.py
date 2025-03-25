# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # big enough
        def func(number):

            total = count = 0
            for weight in weights:
                if total+weight > number:
                    count += 1
                    total = weight
                else:
                    total += weight

            count += 1
            return count <= days


        left = max(weights)
        right = sum(weights)
      
        
        while left<=right:
            mid = (left+right)//2

            if func(mid):
                right = mid-1
                
            else:
                left = mid+1

        return left        