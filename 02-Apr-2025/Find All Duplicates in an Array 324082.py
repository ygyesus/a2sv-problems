# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # visited = set()
        # answer = []

        # for number in nums:
        #     if number in visited:
        #         answer.append(number)
        #         continue
        #     visited.add(number)

        # return answer


        answer = []
        for i in range(len(nums)):

            current = i
            shouldBeAt = nums[i]-1

            while current != shouldBeAt:

                nums[current], nums[shouldBeAt] = nums[shouldBeAt], nums[current]
                if nums[current] == nums[shouldBeAt] and current != shouldBeAt:
                    break
                current = i
                shouldBeAt = nums[i]-1
        # print("SORTED:", nums)
        for i in range(len(nums)):
            if nums[i]-1 != i:
                # print(i, nums[i])
                answer.append(nums[i])

        return answer