# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        def check(i, ladders):
            subArray = []
            for j in range(1, i+1):
                diff = heights[j] - heights[j-1]
                if diff>0:
                    subArray.append(diff)

            subArray.sort()

            while ladders and subArray:
                subArray.pop()
                ladders -= 1
            
            return sum(subArray) <= bricks

        
        left, right = 0, len(heights)-1
        ans = 0
        while left<=right:
            mid = (left+right)//2

            if check(mid, ladders):
                ans = mid
                left = mid+1
            else:
                right = mid-1

        return ans

        
