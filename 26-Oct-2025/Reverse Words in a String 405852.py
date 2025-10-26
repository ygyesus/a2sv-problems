# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        
        words = [word for word in words if word][::-1]

        return ' '.join(words)

