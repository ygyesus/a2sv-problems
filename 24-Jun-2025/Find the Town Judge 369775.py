# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n==1:
                return 1
        count = defaultdict(int)
        trusters = set()
        for truster, trusted in trust:
            count[trusted] += 1
            trusters.add(truster)

        for trusted in count:
            if count[trusted] == n-1 and trusted not in trusters:
                return trusted

        return -1