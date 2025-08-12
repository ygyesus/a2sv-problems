# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans = 0

        for potentialFactor in range(1, n+1):
            ans += n%potentialFactor==0
            if ans==k: return potentialFactor

        return -1