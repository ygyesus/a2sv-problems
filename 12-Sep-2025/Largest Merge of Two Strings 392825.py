# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []

        word1 = deque(word1)
        word2 = deque(word2)

        while word1 or word2:
            if word1>=word2:
                merge.append(word1.popleft())
            elif word2>word1:
                merge.append(word2.popleft())

        return ''.join(merge)