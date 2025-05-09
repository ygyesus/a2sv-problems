# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        def SUM(n):
            total = n*(n+1)//2
            return total
        def binarySearch(n):
            left, right = 1, n
            ans = float('-inf')
            while left<=right:
                mid = (left + right)//2
                total = SUM(mid)
                if total <= n:
                    ans = max(ans, mid)
                    left = mid+1
                else:
                    right = mid-1

            return ans

        ans = binarySearch(n)
        return ans
