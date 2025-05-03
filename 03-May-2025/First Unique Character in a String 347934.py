# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)

        for i in range(len(s)):
            char = s[i]
            if freq[char] == 1:
                return i

        return -1 
