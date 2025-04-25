# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        
        rows, cols = len(targetGrid), len(targetGrid[0])

        boundaries = defaultdict(lambda: [
            float('inf'), float('-inf'), float('inf'), float('-inf')
        ]) # [t, b, l, r]

        for row in range(rows):
            for col in range(cols):

                color = targetGrid[row][col]
                # t
                boundaries[color][0] = min(boundaries[color][0], row)
                # b
                boundaries[color][1] = max(boundaries[color][1], row)
                # l
                boundaries[color][2] = min(boundaries[color][2], col)
                # r
                boundaries[color][3] = max(boundaries[color][3], col)

        graph = defaultdict(list)
        incoming = defaultdict(int)
        for color in boundaries:
            incoming[color]
            top, bottom, left, right = boundaries[color]

            for row in range(top, bottom+1):
                for col in range(left, right+1):
                    new_color = targetGrid[row][col]

                    if new_color != color:
                        graph[color].append(new_color)
                        incoming[new_color] += 1


        q = deque()
        for color in incoming:
            if not incoming[color]:
                q.append(color)
                
        ans = []

        while q:
            color = q.popleft()
            ans.append(color)

            for neighbor in graph[color]:
                incoming[neighbor] -= 1
                
                # any nodes taking part in cycles never get visited, because
                # their indegrees are always at least one
                if incoming[neighbor] == 0:
                    q.append(neighbor)

        return len(ans) == len(boundaries)
        


