# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        incoming = [0 for _ in range(numCourses)]

        graph = defaultdict(list)
        for nextCourse, prevCourse in prerequisites:
            incoming[nextCourse] += 1
            graph[prevCourse].append(nextCourse)

        
        q = deque()

        for course in range(numCourses):
            if incoming[course] == 0:
                q.append(course)

        order = []

        while q:
            course = q.popleft()
            order.append(course)

            for neighbor in graph[course]:
                incoming[neighbor] -= 1

                if incoming[neighbor] == 0:
                    q.append(neighbor)

        return order if len(order) == numCourses else []

            