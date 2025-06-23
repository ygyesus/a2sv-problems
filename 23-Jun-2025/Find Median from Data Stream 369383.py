# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

        for x in (self.small, self.large):
            heapify(x)

    def addNum(self, num: int) -> None:
        heappush(self.large, num)



        while len(self.large) > len(self.small):
            x = heappop(self.large)
            heappush(self.small, -x)

        while self.large and self.small and -self.small[0]>self.large[0]:
            largeInSmall = -heappop(self.small)
            smallInLarge = heappop(self.large)

            heappush(self.large, largeInSmall)
            heappush(self.small, -smallInLarge)


    def findMedian(self) -> float:
        if (len(self.small)+len(self.large))%2==1:
            median = -self.small[0]
            return median

        left = -self.small[0]
        right = self.large[0]

        median = (left+right)/2
        return median

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()