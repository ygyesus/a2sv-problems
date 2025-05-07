# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for i in range(1, len(words)):

            word = words[i]
            counter = Counter(word)

            for order in range(ord('a'), ord('z')+1):
                char = chr(order)
                common[char] = min(common[char], counter[char])


        ans = []

        for char in common:
            while common[char]:
                ans.append(char)
                common[char] -= 1
        
        return ans 