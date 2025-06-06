# Problem: Get Maximum in Generated Array - https://leetcode.com/problems/get-maximum-in-generated-array/description/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0: return 0
        # maxNum = 1


        arr = [0,1]

        for i in range(2,n+1):
            if i%2==0:
                arr.append(arr[i//2])
            else:  
                i = i//2
                arr.append(arr[i] + arr[i+1])
        # print(arr)
        return max(arr)