# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n+1):
            total = 0
            while i:
                if i%2:
                    total += 1
                i = i>>1

            ans.append(total)

        return ans


