# Problem: House Robber IV - https://leetcode.com/problems/house-robber-iv/

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        def check(capability):

            stack1 = []
            stack2 = []

            curr = stack1
            for i in range(len(nums)):

                if nums[i] <= capability:

                    if stack1 and stack1[-1]+1 == i:
                        stack2.append(i)
                        continue
                    elif stack2 and stack2[-1] + 1 == i:
                        stack1.append(i)
                        continue

                    if len(stack1) > len(stack2):
                        stack1.append(i)
                    else:
                        stack2.append(i)

            return max(len(stack1), len(stack2)) >= k


        left, right = 0, 10**9 * len(nums)
        ans = None

        while left<=right:
            capability = (left+right)//2

            if check(capability):
                ans = capability
                right = capability - 1
            else:
                left = capability + 1

        # print(left, right)

        return ans
