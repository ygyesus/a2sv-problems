# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        hatred = defaultdict(set)

        for hater, hated in dislikes:
            hatred[hater].add(hated)
            hatred[hated].add(hater)

        groups = {
            0:  set(),
            1:  set()
        }

        visited = set()
        def dfs(x, hater):

            if hater in visited:
                return True

            if groups[x].intersection(hatred[hater]):
                return False

            groups[x].add(hater)
            visited.add(hater)

            for num in hatred[hater]:
                if not dfs(1-x, num):
                    return False

            return True

        
        for num in range(1,n+1):
            if not dfs(0,num):
                return False

        return True



        

