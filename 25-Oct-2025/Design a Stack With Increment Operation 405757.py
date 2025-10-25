# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize: self.stack.append(x)

    def pop(self) -> int:
        if not self.stack: return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if not i<len(self.stack): return
            self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)