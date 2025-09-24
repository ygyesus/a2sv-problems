# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            i=0
            j=len(row)-1

            while i<j:
                row[i], row[j] = row[j], row[i]
                i+=1
                j-=1

        for row in image:
            for rowIndex in range(len(image)):
                if row[rowIndex] == 0:
                    row[rowIndex] = 1
                elif row[rowIndex] == 1:
                    row[rowIndex] = 0

        return image


        