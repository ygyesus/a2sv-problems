# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda point: point[-1])

        count = 0
        lastBurst = points[0][1]

        for i in range(len(points)):
            l,r = points[i]

            if l<=lastBurst:
                pass
            else:
                count += 1
                lastBurst = r

        return count+1