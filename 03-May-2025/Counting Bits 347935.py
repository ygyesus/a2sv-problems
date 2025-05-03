# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for num in range(n+1):
            bits = bin(num)
            bits = list(bits)

            bits.pop(0)
            bits.pop(0)
            bits = list(map(int, bits))
            total = sum(bits)
            ans.append(total)

        return ans