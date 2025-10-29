# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        
        def forward(vowelIndex):
            nextChars = n-1 - vowelIndex
            return 1+nextChars

        def backward(vowelIndex):
            prevChars = vowelIndex
            return 1+prevChars

        vowels = ['a', 'e', 'i', 'o', 'u']

        ans = 0
        for i in range(n):
            if word[i] in vowels:
                ans += forward(i) * backward(i)

        return ans