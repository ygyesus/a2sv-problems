# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordToFreq = defaultdict(int)

        for word in words:
            wordToFreq[word] += 1

        freqToWords = defaultdict(list)

        for word in wordToFreq:
            freq = wordToFreq[word]
            freqToWords[freq].append(word)

        for freq in freqToWords:
            freqToWords[freq].sort()

        freqs = list(freqToWords.keys())
        freqs.sort(key = lambda k: -k)

        ans = []
        for freq in freqs:
            if not k: break
            for word in freqToWords[freq]:
                ans.append(word)
                k -= 1
                if not k: break

        return ans


            


        

