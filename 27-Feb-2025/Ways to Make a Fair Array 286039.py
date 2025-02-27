# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        evens = []

        odds = []

        sumOfEvens = sumOfOdds = ans = 0
        for i,num in enumerate(nums):
            if i%2:
                sumOfOdds += num
            else:
                sumOfEvens += num

            evens.append(sumOfEvens)
            odds.append(sumOfOdds)

        
        for i,num in enumerate(nums):
            # IF ODD
            if i%2:
                # LEFTEVENSUM and LEFTODDSUM stay the same

                leftEvenSum = evens[i-1] if i>0 else 0
                leftOddSum = odds[i-1] if i>0 else 0

                # RIGHTEVENSUM is RIGHTODDSUM and vice versa

                rightEvenSum = sumOfOdds - leftOddSum - nums[i]
                rightOddSum = sumOfEvens -leftEvenSum

            else:
                leftEvenSum = evens[i-1] if i>0 else 0
                leftOddSum = odds[i-1] if i>0 else 0
                
                rightEvenSum = sumOfOdds - leftOddSum
                rightOddSum = sumOfEvens -leftEvenSum - nums[i]

            if leftEvenSum+rightEvenSum == leftOddSum + rightOddSum:
                ans += 1

        return ans

