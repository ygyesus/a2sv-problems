# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        saved = []
        for i, (a,b) in enumerate(costs):
            saved.append(((a-b), i, 'a'))

        saved.sort()

        total = 0
        for i in range(2*n):
            trio = saved[i]

            index = trio[1]
            if i<n:
                total += costs[index][0]
            else:
                total += costs[index][1]

        return total


        