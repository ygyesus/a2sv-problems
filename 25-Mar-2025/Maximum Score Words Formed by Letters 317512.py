# Problem: Maximum Score Words Formed by Letters - https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        maxLetterFreq = Counter(letters)
        n = len(words)
        DICT = defaultdict(int)

        maxScore = [0]
        def backtrack(start, scoreSoFar, DICT):
            originalDICT = Counter(DICT)

            for i in range(start+1, n):
                word = words[i]
                wordScore = 0
                for char in word:
                    if DICT[char] >= maxLetterFreq[char]:
                        DICT = Counter(originalDICT)
                        wordScore = 0
                        break
                    charIndex = ord(char) - ord('a')
                    wordScore += score[charIndex]
                    DICT[char] += 1

                maxScore[0] = max(maxScore[0], scoreSoFar + wordScore)
                if wordScore == 0:
                    continue

                backtrack(i, scoreSoFar + wordScore, DICT)
                DICT = Counter(originalDICT)

        
        backtrack(-1, 0, DICT)
        return maxScore[0]

                

                

                
