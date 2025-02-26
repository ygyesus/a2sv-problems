# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:


        total = 0

        indices = defaultdict(list)

        
        maxLength = 0

        for i,num in enumerate(nums):
            if num==1:
                total += 1
            else:
                total -= 1
                

            indices[total].append(i)

            if total==0:
                maxLength = max(maxLength, i+1)

        for total in indices:
            if len(indices[total]) > 1:
                maxLength = max(indices[total][-1] - indices[total][0], maxLength)

        return maxLength