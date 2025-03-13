# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        for i in range(len(self.queue1)-1, -1, -1):
            self.queue2.append(self.queue1[i])

        x = self.queue2.pop(0)

        self.queue1 = []
        for i in range(len(self.queue2)-1, -1, -1):
            self.queue1.append(self.queue2[i])
        self.queue2 = []
        return x
        
        
    def top(self) -> int:
        for i in range(len(self.queue1)-1, -1, -1):
            self.queue2.append(self.queue1[i])

        x = self.queue2[0]
        self.queue1 = []
        for i in range(len(self.queue2)-1, -1, -1):
            self.queue1.append(self.queue2[i])
        self.queue2 = []
        return x
    def empty(self) -> bool:
        return not self.queue1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()