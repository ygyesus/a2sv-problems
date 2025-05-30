# Problem: Delete Columns to Make Sorted - https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        cols = len(strs[0])

        ans = 0
        for col in range(cols):
            for i in range(1,len(strs)):
                curr = strs[i][col]
                prev = strs[i-1][col]

                if prev>curr:
                    ans+=1
                    break

        return ans
                