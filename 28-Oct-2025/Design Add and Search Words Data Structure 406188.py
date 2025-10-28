# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.word_exists = False
        self.children = [None] * 26

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            i = ord(char) - ord('a')
            if not curr.children[i]: curr.children[i] = TrieNode()
            curr = curr.children[i]

        curr.word_exists = True

    def search(self, word: str) -> bool:
        
        def dfs(curr, word):
            if not word: return curr.word_exists

            if word[0] != '.':
                i = ord(word[0]) - ord('a')
                if not curr.children[i]: return False
                return dfs(curr.children[i], word[1:])

            else:
                for child in curr.children:
                    if not child: continue
                    if dfs(child, word[1:]): return True
            
            return False

        return dfs(self.root, word)





        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)