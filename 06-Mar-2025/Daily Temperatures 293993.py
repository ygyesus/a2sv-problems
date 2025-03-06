# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        ans = []
        mapping = defaultdict(deque)

        for i,temp in enumerate(temperatures):
            while stack and stack[-1] < temp:
                mapping[stack[-1]].append(i)
                stack.pop()

            stack.append(temp)

        
        for i, num in enumerate(temperatures):
            if not mapping[num]:
                ans.append(0)

            else:
                dest = mapping[num].popleft()
                ans.append(dest-i)

        return ans