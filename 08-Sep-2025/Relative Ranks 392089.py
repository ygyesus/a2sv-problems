# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        SORTED = sorted(score, key = lambda x: -x)

        ans = {}
        for i, num in enumerate(SORTED):
            ans[num] = i+1
            if i+1==1: ans[num] = "Gold Medal"
            elif i+1==2: ans[num] = "Silver Medal"
            elif i+1==3: ans[num] = "Bronze Medal"

        return [str(ans[num]) for num in score]