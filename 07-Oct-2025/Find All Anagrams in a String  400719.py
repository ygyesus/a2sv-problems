# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        counterP = Counter(p)
        ans = []
        freq = Counter(s[:n])
        if freq == counterP: ans.append(0)
        left = 0
        for right in range(n, len(s)):
            freq[s[left]] -= 1
            if not freq[s[left]]: del freq[s[left]]
            left += 1
            freq[s[right]] += 1
            if freq == counterP: ans.append(left)

        return ans
            