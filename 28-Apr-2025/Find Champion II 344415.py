# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        
        # eliminate weak nodes
        # decrease for those one step above them
        if n==1: return 0
        graph = defaultdict(list)
        visited = set()


        incoming = defaultdict(int)
        for strong, weak in edges:
            incoming[weak] += 1
            graph[weak].append(strong)
            visited.add(weak)
            visited.add(strong)

        if not len(visited) == n: return -1

        q = deque()

        for node in range(n):
            if incoming[node] == 0:
                q.append(node)


        ans = None
        while q:
            ans = list(q)
            for _ in range(len(q)):
                weaker = q.popleft()

                for stronger in graph[weaker]:
                    incoming[stronger] -= 1
                    if incoming[stronger] == 0:
                        q.append(stronger)


        if len(ans) == 1:
            return ans.pop()

        return -1

                
                

            
    
        
