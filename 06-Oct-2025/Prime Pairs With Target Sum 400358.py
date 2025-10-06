# Problem: Prime Pairs With Target Sum - https://leetcode.com/problems/prime-pairs-with-target-sum/description/

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        isPrime = [True for _ in range(n+1)]

        isPrime[0] = False
        if 1<n: isPrime[1] = False

        for prime in range(2, n+1):
            if isPrime[prime]:
                for multiple in range(2*prime, n+1, prime):
                    isPrime[multiple] = False

        left, right = 0, n
        ans = []
        while left<=right:
            if isPrime[left] == isPrime[right] == True:
                ans.append([left, right])
            left += 1
            right -= 1

        return ans
