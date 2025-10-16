# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.score = 0

class MapSum:
    def __init__(self):
        self.map = {}
        self.root = TrieNode()
        
    def insert(self, key: str, val: int) -> None:
        curr = self.root

        for char in key:
            i = ord(char)-ord('a')
            if not curr.children[i]:
                curr.children[i] = TrieNode()
            curr = curr.children[i]

        curr.score = val
        
    def sum(self, prefix: str) -> int:

        total = 0
        curr = self.root
        for char in prefix:
            i = ord(char)-ord('a')
            if not curr.children[i]:
                curr.children[i] = TrieNode()
            curr = curr.children[i]

        stack = [curr]
        total = 0
        while stack:
            curr = stack.pop()
            total += curr.score
            for child in curr.children:
                if child: stack.append(child)
        return total



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)