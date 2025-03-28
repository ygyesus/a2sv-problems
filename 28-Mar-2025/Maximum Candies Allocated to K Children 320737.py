# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candies.sort()
        def check(num):

            totalQuotients = 0
            for candy in candies:
                totalQuotients += candy//num

            return totalQuotients >= k
                
        left, right = 1, sum(candies)//k

        ans = 0
        while left<=right:
            mid = (left+right)//2

            if check(mid):
                left = mid+1
                ans = mid
            else:
                right = mid-1

        return ans


