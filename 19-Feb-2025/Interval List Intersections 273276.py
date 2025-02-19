# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        def getIntersectionInterval(firstList, secondList):
            return [
                max(firstList[0], secondList[0]),
                min(firstList[1], secondList[1])
            ]

        
        ans = []
        
        i=j=0

        while i<len(firstList) and j<len(secondList):

            firstInterval = firstList[i]
            secondInterval = secondList[j]

            if firstInterval[1]<secondInterval[0]:
                i+=1
                continue
            elif secondInterval[1]<firstInterval[0]:
                j+=1
                continue

            # if intersectionExists(firstInterval, secondInterval):
            intersection = getIntersectionInterval(firstInterval, secondInterval)
            ans.append(intersection)
            if firstInterval[1] < secondInterval[1]:
                i+=1
            else:
                j+=1


        return ans