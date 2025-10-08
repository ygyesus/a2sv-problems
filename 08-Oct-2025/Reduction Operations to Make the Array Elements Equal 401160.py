# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()

        counter = Counter(nums)

        values = list(counter.values())

        n = len(values)

        totalOps = 0
        for i in range(n-1, 0, -1):
            ops = values[i]
            totalOps += ops
            values[i-1] += values[i]

        return totalOps


