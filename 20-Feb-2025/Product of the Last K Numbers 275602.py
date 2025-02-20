# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.prefix = []
        self.product = 1
        self.latestZero = None

    def add(self, num: int) -> None:
        self.stream.append(num)

        if num==0:
            self.latestZero = len(self.stream)-1
            self.product = 1
            self.prefix.append(1)

        else:
            self.product *= num
            self.prefix.append(self.product)


    def getProduct(self, k: int) -> int:
        start = len(self.stream)-k
       
        if self.latestZero != None and self.latestZero >= len(self.stream)-k:
       
            return 0
        
        divideBy = self.prefix[len(self.prefix)-k-1] if len(self.prefix)>=k+1 else 1

        ans = self.product//divideBy
        return ans
        
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)