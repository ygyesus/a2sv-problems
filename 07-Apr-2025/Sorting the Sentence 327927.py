# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        
        s = s.split()

        LIST = [None] * len(s)

        for word in s:
            index = int(word[-1])
            word = word[:-1]

            LIST[index-1] = word

        return " ".join(LIST)