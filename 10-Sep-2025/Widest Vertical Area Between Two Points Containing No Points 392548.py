# Problem: Widest Vertical Area Between Two Points Containing No Points - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = [x for x, _ in points]
        points.sort()

        maxDiff = 0

        for i in range(1, len(points)):
            diff = points[i] - points[i-1]
            maxDiff = max(maxDiff, diff)

        return maxDiff