# Problem: Implement stack using queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:

        self.queue = self.queue[::-1]
        x = self.queue.pop(0)
        self.queue = self.queue[::-1]
        return x
        
    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()