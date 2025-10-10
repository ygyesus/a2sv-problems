# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.freqOfNum = Counter()
        self.freqOfFreq = Counter()

    def add(self, number: int) -> None:
        originalFreq = self.freqOfNum[number]
        self.freqOfFreq[originalFreq] -= 1
        if not self.freqOfFreq[originalFreq]:
            del self.freqOfFreq[originalFreq]
        self.freqOfNum[number] += 1
        newFreq = self.freqOfNum[number]
        self.freqOfFreq[newFreq] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.freqOfNum:

            originalFreq = self.freqOfNum[number] 
            self.freqOfFreq[originalFreq] -= 1
            self.freqOfNum[number] -= 1
            if not self.freqOfFreq[originalFreq]:
                del self.freqOfFreq[originalFreq]
            if not self.freqOfNum[number]:
                del self.freqOfNum[number]
            newFreq = originalFreq-1
            if newFreq:
                self.freqOfFreq[newFreq] += 1
            

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freqOfFreq
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)