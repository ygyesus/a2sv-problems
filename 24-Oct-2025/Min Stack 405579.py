# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.indices = {}
        self.mins = []
    
    def push(self, val):
        i = len(self.stack)
        if not val in self.indices: self.indices[val] = []
        self.indices[val].append(i)
        self.stack.append(val)
        if not self.mins or val<self.mins[-1]:
            self.mins.append(val)

    def pop(self):
        val = self.stack[-1]
        self.stack.pop()
        self.indices[val].pop()

        if not self.indices[val]: 
            del self.indices[val]
            if val == self.mins[-1]: self.mins.pop()
                
    def getMin(self):
        return self.mins[-1]
        

    def top(self):
        return self.stack[-1]