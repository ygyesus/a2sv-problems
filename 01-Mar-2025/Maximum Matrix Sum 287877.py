# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        
        zeroExists = False

        minWholeNumber = (float('inf'), None, None)
        negativeCount = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                num = matrix[i][j]

                if num < 0:
                    negativeCount += 1
                elif num == 0:
                    zeroExists = True
                
                if abs(num)<abs(minWholeNumber[0]):
                    minWholeNumber = (num,i,j)

        if negativeCount%2 == 1:
            if zeroExists:
                for i in range(len(matrix)):
                    for j in range(len(matrix[i])):
                        matrix[i][j] = abs(matrix[i][j])

            else:
                i,j = minWholeNumber[1], minWholeNumber[2]

                matrix[i][j] = -1*abs(matrix[i][j])

                for x in range(len(matrix)):
                    for y in range(len(matrix[i])):
                        if not (x,y) == (i,j):
                            matrix[x][y] = abs(matrix[x][y])

        else:
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    matrix[i][j] = abs(matrix[i][j])


        total = 0

        for row in matrix:
            for num in row:
                total += num


        return total