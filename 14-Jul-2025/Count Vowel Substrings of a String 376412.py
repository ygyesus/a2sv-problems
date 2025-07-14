# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        ans = 0
        for i in range(len(word)):
            for j in range(len(word)):
                ans += set(word[i:j+1]) == vowels

        return ans
