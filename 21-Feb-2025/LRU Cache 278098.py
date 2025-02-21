# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.cache = {}
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        else:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                for someKey in self.cache:
                    del self.cache[someKey]
                    break
            self.cache[key] = value
                    
                    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)