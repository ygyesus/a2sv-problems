# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        visited = set()

        def getDistance(x1, y1, x2, y2):
            return ((x1-x2)**2 + (y1-y2)**2)**0.5

        def dfs(curr):
            x,y,radius = bombs[curr]
            visited.add(curr)

            for i in range(len(bombs)):
                if i in visited: continue
                new_x,new_y,new_radius = bombs[i]
                distance = getDistance(x, y, new_x, new_y)
                if distance>radius: continue
                dfs(i)


        maxCount = float('-inf')

        for i in range(len(bombs)):
            dfs(i)
            print(visited)
            count = len(visited)
            maxCount = max(maxCount, count)

            visited = set()

        return maxCount

        

            