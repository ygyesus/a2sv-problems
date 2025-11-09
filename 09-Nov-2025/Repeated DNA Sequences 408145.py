# Problem: Repeated DNA Sequences - https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left, right, n = 0, 10, len(s)

        counter = Counter()
        while right<=n:
            string = s[left:right]
            counter[string] += 1
            left+=1
            right+=1

        ans = [key for key in counter.keys() if counter[key]>1]
        return ans
