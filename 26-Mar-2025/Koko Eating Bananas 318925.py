# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def validate(k):
    
            total = 0
            
            for i in range(len(piles)):
                total += piles[i]//k
                if piles[i]%k:
                    total += 1

            print("hours:", total)
            return total <= h

        left = 1
        right = max(piles)

        while left<=right:
            mid = (left+right)//2
            # print(mid)

            if validate(mid):
                right = mid-1
            else:
                left = mid+1

        return left