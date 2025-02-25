# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = defaultdict(list)

        total = 0
        visitedRemainders = defaultdict(list)
        
        for i,num in enumerate(nums):
            total += num
            
            if i>0:
                if total%k in visitedRemainders:
                    if visitedRemainders[total%k][0] <= i - 2:
                        return True
                
                if total%k==0:
                    print(2)
                    return True

            visitedRemainders[total%k].append(i)



        print(remainders)

        return False
