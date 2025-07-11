# Problem: Find the Middle Index in Array - https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0]

        for num in nums:
            total = prefix[-1] + num
            prefix.append(total)

        for i in range(len(nums)):
            leftSum = prefix[i]
            rightSum = prefix[-1] - prefix[i+1]

            if leftSum==rightSum:
                return i

        return -1