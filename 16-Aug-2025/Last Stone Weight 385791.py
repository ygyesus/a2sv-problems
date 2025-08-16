# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): stones[i] *= -1

        heapify(stones)

        while len(stones)>=2:
            y = heappop(stones)
            x = heappop(stones)
            if x==y: continue

            else: 
                # diff has to remain negative as all the others are negative
                diff = (y-x) 
                heappush(stones, diff)

        if stones: return -heappop(stones)
        return 0