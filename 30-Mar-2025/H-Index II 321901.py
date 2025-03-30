# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def check(h):

            count = 0

            for citation in citations:
                if citation >= h:
                    count += 1
                    if count >= h:
                        return True

            return False

        n = len(citations)
        left, right = 0, n

        while left<=right:
            mid = (left+right)//2
            # print(left, right, mid)

            if check(mid):
                left = mid+1
                ans = mid
            else:
                right = mid-1

        return ans

        