# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        n = len(arr)

        LIST = []
        maxAns = 0
        for i in range(1, n):
            if arr[i-1] < arr[i]:
                if not LIST or LIST[-1] == '>':
                    LIST.append('<')
                else:
                    LIST = ['<']
            elif arr[i-1] > arr[i]:
                if not LIST or LIST[-1] == '<':
                    LIST.append('>')
                else:
                    LIST = ['>']
            else:
                ans = len(LIST)
                maxAns = max(maxAns, ans)
                LIST = []
        
            ans = len(LIST)
            maxAns = max(maxAns, ans)

        print(LIST)
        return 1+maxAns



