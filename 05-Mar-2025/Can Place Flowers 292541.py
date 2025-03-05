# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total = 0

        temp = 0
        lastOne = -1
        
        if flowerbed[0] == 0:
            if len(flowerbed)==1 or (len(flowerbed)>1 and flowerbed[1] == 0):
                total += 1 
                lastOne = 0
        

        for i,num in enumerate(flowerbed):
            if num == 0 and i==lastOne+2:
                if (not i+1 < len(flowerbed) or flowerbed[i+1] == 0):
                    total += 1
                    lastOne = i
                    print(total, i)
                    
            else:
                if num == 1:
                    lastOne = i

        return total >= n
                