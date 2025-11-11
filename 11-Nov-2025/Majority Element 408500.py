# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for x in nums:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
            
            if dict[x] > len(nums)/2:
                return x
                
            
            