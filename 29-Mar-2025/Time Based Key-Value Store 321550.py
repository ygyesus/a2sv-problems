# Problem: Time Based Key-Value Store - https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        if not key in self.map:
            return ""

        timestamps = self.map[key]

        i = bisect_right(timestamps, (timestamp, 'zzzz'*10**2))
        
        if i>0:
            return timestamps[i-1][-1]
        return ""


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)