# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        offset = trips[0][1]
        maximum = trips[0][2]
        for numPassengers, FROM, TO in trips:
            offset = min(offset, FROM)
            maximum = max(maximum, TO)

    
        prefix = [0 for _ in range(offset, maximum+1)]

        for numPassengers, FROM, TO in trips:
            prefix[FROM-offset] += numPassengers

            if TO - offset < len(prefix):
                prefix[TO-offset]-=numPassengers

        
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]

        for num in prefix:
            if num>capacity:
                return False

        return True
