# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)

        sentence = sentence.split()

        for i in range(len(sentence)):
            word = sentence[i]

            j = 0
            prefix = ""
            while j<len(word):
                if prefix in dictionary:
                    sentence[i] = prefix
                    break

                else:
                    prefix += word[j]
                    j += 1

        return ' '.join(sentence)