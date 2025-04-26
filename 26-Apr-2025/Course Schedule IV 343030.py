# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)

        incoming = defaultdict(int)
        for prevCourse, nextCourse in prerequisites:

            graph[prevCourse].append(nextCourse)
            incoming[nextCourse] += 1

        q = deque()
        for course in range(numCourses):
            if incoming[course] == 0: 
                q.append(course)


        def dfs(course, target):
            if course == target:
                return True

            visited.add(course)

            for neighbor in graph[course]:
                if neighbor in visited: continue
                if dfs(neighbor, target):
                    return True

            return False

        ans = []
        for prevCourse, nextCourse in queries:
            visited = set()
            if dfs(prevCourse, nextCourse):
                ans.append(True)
            else:
                ans.append(False)

        return ans

