# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        
        other = 1<<(num.bit_length())
        other -= 1

        return num ^ other