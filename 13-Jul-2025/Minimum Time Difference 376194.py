# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        totalMinutes = 24*60

        # timePoints = set(timePoints)

        def func(timePoint):
            hours, minutes = timePoint.split(':')
            hours = int(hours)
            minutes = int(minutes)

            return hours*60 + minutes

        def getMin(diff):
            return min(abs(diff), totalMinutes-abs(diff))

        for i in range(len(timePoints)):
            timePoints[i] = func(timePoints[i])

        timePoints.sort()

        minimum = getMin(timePoints[0] - timePoints[-1])

        for i in range(1, len(timePoints)):
            diff = getMin(timePoints[i] - timePoints[i-1])
            minimum = min(minimum, diff)

        return minimum

        