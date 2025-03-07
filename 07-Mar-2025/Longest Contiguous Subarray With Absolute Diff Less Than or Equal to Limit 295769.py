# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        minimum = deque()
        maximum = deque()

        left = 0
        ans = 0
        for right in range(len(nums)):
            i = right
            while minimum and nums[minimum[-1]] > nums[i]:
                minimum.pop()

            while maximum and nums[maximum[-1]] < nums[i]:
                maximum.pop()

            minimum.append(i)
            maximum.append(i)

            while minimum and maximum and nums[maximum[0]] - nums[minimum[0]] > limit:
                if maximum[0] < minimum[0]:
                    left = maximum.popleft()+1
                else:
                    left = minimum.popleft() + 1



            ans = max(ans, right-left+1)

        return ans        
