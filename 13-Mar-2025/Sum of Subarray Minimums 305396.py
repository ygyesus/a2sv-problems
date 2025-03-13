# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        def getPreviousSmaller(a):
            previousSmaller = {}
            stack = []
            for i in range(n):
                while stack and a[stack[-1]] >= a[i]:
                    stack.pop()

                if stack:
                    previousSmaller[i] = stack[-1]

                stack.append(i)

            return previousSmaller

        def getNextSmaller(a):
            nextSmaller = {}
            stack = []

            for i in range(n):
                while stack and a[stack[-1]] >= a[i]:
                    nextSmaller[stack.pop()] = i
                    
                stack.append(i)

            return nextSmaller

        previousSmaller = getPreviousSmaller(arr)
        nextSmaller = getNextSmaller(arr)
        ans = 0

        for i in range(n):
            L = previousSmaller[i] if i in previousSmaller else -1
            R = nextSmaller[i] if i in nextSmaller else n

            ans += ((i-L) * (arr[i]) * (R-i)) 

        print("previousSmaller:", previousSmaller)
        print("nextSmaller:", nextSmaller)
        return ans%(10**9 + 7)

