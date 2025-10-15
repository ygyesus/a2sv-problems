# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.word_exists = False
        self.children = [None for _ in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            i = ord(char.lower()) - ord('a')
            if not curr.children[i]:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.word_exists = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            i = ord(char.lower()) - ord('a')
            if not curr.children[i]: return False
            curr = curr.children[i]
        return curr.word_exists

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for char in prefix:
            i = ord(char.lower()) - ord('a')
            if not curr.children[i]: return False
            curr = curr.children[i]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)