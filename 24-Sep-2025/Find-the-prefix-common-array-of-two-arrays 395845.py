# Problem: Find-the-prefix-common-array-of-two-arrays - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = []

        for i in range(n):
            count = 0
            for j in range(i+1):
                count += A[j] in B[:i+1]

            ans.append(count)

        return ans

            