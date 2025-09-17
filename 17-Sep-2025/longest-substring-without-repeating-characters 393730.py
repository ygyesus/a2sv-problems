# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)
        
        visited = set()
        
        max_ans = 0
        freq = defaultdict(int)

        left = 0
        for right in range(len(s)):
            char = s[right]
            freq[char] += 1

            while freq[char] > 1:
                freq[s[left]] -= 1
                left += 1


            max_ans = max(max_ans, right-left+1)

        return max_ans