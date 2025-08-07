# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def processArr(arr):
            arr.insert(0,0)
            arr.append(0)

            newArr = []
            n = len(arr)
            for i in range(1, n):
                total = arr[i] + arr[i-1]
                newArr.append(total)

            arr.pop(0)
            arr.pop()

            return newArr

        arr = [1]

        if numRows==1: return [[1]]


        ans = [[1]]

        for i in range(numRows-1):
            newArr = processArr(ans[-1])
            ans.append(newArr)

        return ans

    

