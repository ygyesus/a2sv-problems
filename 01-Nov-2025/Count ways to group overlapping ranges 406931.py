# Problem: Count ways to group overlapping ranges - https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ranges.sort()
        n = len(ranges)
        MIN, MAX = ranges[0]
        count = 0

        for j in range(1, n):
            c, d = ranges[j]

            if MIN<=c<=MAX:
                MIN = min(MIN, c)
                MAX = max(MAX, d)
                
            else:
                MIN, MAX = c, d
                count += 1
        count += 1
        ans = (1<<count)%MOD
        return ans
        

