# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(list)

        for i in range(n):
            graph[manager[i]].append(i)

            

        
        def dfs(emp):
            maxTotal = 0
            for sub in graph[emp]:
                total = dfs(sub)
                maxTotal = max(maxTotal, total)

            return maxTotal + informTime[emp]

        return dfs(headID)

        