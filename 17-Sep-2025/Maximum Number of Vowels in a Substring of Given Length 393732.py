# Problem: Maximum Number of Vowels in a Substring of Given Length - https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for i in range(k):
            count += (s[i] in vowels)
        maxCount = count

        n = len(s)
        left = 0
        for right in range(k, n):
            count -= (s[left] in vowels)
            left += 1
            count += (s[right] in vowels)

            maxCount = max(maxCount, count)

        return maxCount

            


        