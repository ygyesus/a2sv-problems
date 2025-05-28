# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        ans = []

        maxNum = float('-inf')
        for i in range(len(arr)-1, 0, -1):
            maxNum = max(maxNum, arr[i])
            ans.append(maxNum)

        ans = ans[::-1]
        ans.append(-1)
        return ans
        