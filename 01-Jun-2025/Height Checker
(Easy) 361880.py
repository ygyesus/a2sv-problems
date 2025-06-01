# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)

        ans = 0

        for i in range(len(heights)):
            ans += (heights[i] != expected[i])

        return ans