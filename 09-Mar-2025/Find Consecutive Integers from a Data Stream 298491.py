# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.value = value
        self.k = k
        self.streak = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.streak += 1
        else:
            self.streak = 0

        if self.streak >= self.k:
            return True
        return False
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)