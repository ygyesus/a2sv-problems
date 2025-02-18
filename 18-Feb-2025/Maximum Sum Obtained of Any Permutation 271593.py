# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0 for _ in range(n)]

        for request in requests:
            i = request[0]
            j = request[1]

            prefix[i] += 1
            if j+1<n:
                prefix[j+1] -= 1


        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        prefix.sort()
        nums.sort()
        # print("PREFIX:", prefix)
        # print("NUMS:", nums)


        ans = 0
        for i in range(len(prefix)):
            ans += prefix[i] * nums[i]
        return ans%(10**9 + 7)