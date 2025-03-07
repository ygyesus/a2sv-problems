# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        def nextGreater(nums):
            n = len(nums)

            ans = [-1] * n
            stack = []
            for i in range(2*n):
                i = i%(n)
                # print("i:", i)
                while stack and nums[stack[-1]] < nums[i]:
                    x = stack.pop()
                    if ans[x] == -1:
                        ans[x] = nums[i]

                stack.append(i)

            return ans

        return nextGreater(nums)