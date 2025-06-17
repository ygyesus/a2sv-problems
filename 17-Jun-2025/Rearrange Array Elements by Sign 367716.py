# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positives = []
        negatives = []

        for num in nums:
            if num>0:
                positives.append(num)
            elif num<0:
                negatives.append(num)

        ans = []

        i = 0

        while i<len(positives):
            ans.append(positives[i])
            ans.append(negatives[i])
            
            i+=1

        return ans