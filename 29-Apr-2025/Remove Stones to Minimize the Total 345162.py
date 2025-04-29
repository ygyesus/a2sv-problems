# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1

        heapq.heapify(piles)

        while k:
            maximum = heapq.heappop(piles)

            maximum *= -1 # POSITIVE

            maximum -= maximum//2

            maximum *= -1 # NEGATIVE

            heappush(piles, maximum)
            k-=1

        # print(piles)

        return sum(piles) * -1