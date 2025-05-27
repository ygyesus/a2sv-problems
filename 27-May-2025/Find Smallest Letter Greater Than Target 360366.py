# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[0]
        if not target in letters:
            letters.append(target)

        letters.sort()

        while letters and letters[-1] != target:
            ans = letters.pop()

        return ans