# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [x for x in nums]
        result = []
        for i in range(1, len(nums)):
            prefix[i] += prefix[i-1]

        print("PREFIX:", prefix)
        for i, num in enumerate(nums):
            # print("============")
            # print(num)
            # print("============")
            rightSum = prefix[-1] - prefix[i]
            rightSide_NumItself = (len(nums)-1-i) * num

            leftSum = prefix[i] - num
            leftSide_NumItself = i*num

            score = rightSum - rightSide_NumItself + leftSide_NumItself - leftSum
            result.append(score)

            # print("rightSum:", rightSum)
            # print("rightSide_NumItself:", rightSide_NumItself)

            # print("leftSum:", leftSum)
            # print("leftSide_NumItself:", leftSide_NumItself)


        return result
