# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allowed = set(allowed)
        def isConsistent(string):
            for char in string:
                if not char in allowed: return False

            return True

        count = 0
        for word in words:
            count += isConsistent(word)

        return count