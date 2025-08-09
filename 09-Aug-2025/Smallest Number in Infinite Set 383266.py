# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [x for x in range(1, 1001)]        
        heapify(self.heap)
    def popSmallest(self) -> int:
        return heappop(self.heap)

    def addBack(self, num: int) -> None:
        if not num in self.heap:
            heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)