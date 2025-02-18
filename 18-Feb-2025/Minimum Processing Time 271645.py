# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(key = lambda x: -x)

        # print(processorTime)
        ans = float('-inf')
        for i in range(3,len(tasks),4):
            task = tasks[i]
            ans = max(ans, processorTime[(i-3)//4] + task)

        return ans