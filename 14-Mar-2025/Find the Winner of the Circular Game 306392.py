# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        # mapping = {x:None for x in range(1,n+1)}
        decimated = 0

        def traverse(arr,start,k):
            count = 0
            while True:
                for i in range(start+1, len(arr)):
                    num = arr[i]
                    if num:
                        count += 1
                        if count == k:
                            arr[i] = 0    
                            return i

                for i in range(start):
                    num = arr[i]
                    if num:
                        count += 1
                        if count == k:
                            arr[i] = 0
                            return i

        arr = [x for x in range(1,n+1)]
        start = -1
        for _ in range(n-1):
            start = traverse(arr, start, k)
            # print(arr)

        for num in arr:
            if num:
                return num

        

            

            


