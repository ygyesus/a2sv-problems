# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        maxAns = 0
        for word1 in words:
            for word2 in words:

                flag = False

                for order in range(ord('a'), ord('z')+1):
                    char = chr(order)
                    if char in word1 and char in word2:
                        flag = True
                        break

                if not flag:
                    ans = len(word1) * len(word2)
                    maxAns = max(maxAns, ans)

        return maxAns