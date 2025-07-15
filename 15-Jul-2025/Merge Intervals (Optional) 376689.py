# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        ans = []

        lastX, lastY = intervals[0]

        for i, interval in enumerate(intervals):
            X, Y = intervals[i]
            if lastX<=X<=lastY or X<=lastX<=Y:
                lastY = max(lastY, Y)
            else:
                ans.append([lastX, lastY])
                lastX, lastY = X, Y

            
        ans.append([lastX, lastY])
        return ans

            