# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        employeeImportance = {}

        for employee in employees:
            emp_id = employee.id
            importance = employee.importance
            subordinates = employee.subordinates

            graph[emp_id].extend(subordinates)
            employeeImportance[emp_id] = importance

        visited = set()
        def dfs(id):
            importance = employeeImportance[id]
            visited.add(id)

            for subordinate in graph[id]:
                if subordinate in visited:
                    continue

                importance += dfs(subordinate)

            return importance

        return dfs(id)

