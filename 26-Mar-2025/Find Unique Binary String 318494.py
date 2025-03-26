# Problem: Find Unique Binary String - https://leetcode.com/problems/find-unique-binary-string/description/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums)
        nums = set(nums)

        def backtrack(string):

            if len(string) == n:
                if string in nums:
                    return None

                return string

            for char in '01':
                zero = backtrack(string + '0')
                one = backtrack(string + '1')

                if zero:
                    return zero
                if one:
                    return one

        return backtrack('')
