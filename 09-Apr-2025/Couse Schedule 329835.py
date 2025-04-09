# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE = 1
        GRAY = 2
        BLACK = 3

        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        colors = [WHITE] * numCourses

        visited = set()

        def dfs(course):

            colors[course] = GRAY

            for neighbor in graph[course]:
                if colors[neighbor] == BLACK:
                    continue

                if colors[course] == colors[neighbor] == GRAY:
                    return False

                if not dfs(neighbor):
                    return False

            colors[course] = BLACK
            return True

        for course in range(numCourses):

            if not dfs(course):
                return False

        return True
        


