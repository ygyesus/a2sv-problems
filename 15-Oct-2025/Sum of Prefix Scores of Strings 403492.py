# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/


class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.score = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        root = TrieNode()

        for word in words:
            curr = root
            for char in word:
                i = ord(char) - ord('a')
                if not curr.children[i]:
                    curr.children[i] = TrieNode()
                curr = curr.children[i]
                curr.score += 1

        ans = []
        for word in words:
            curr = root
            totalScore = 0

            for char in word:
                i = ord(char) - ord('a')
                curr = curr.children[i]
                totalScore += curr.score

            ans.append(totalScore)

        return ans
