# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        prefix = [0]
        
        for num in nums:
            total = prefix[-1] + num
            prefix.append(total)

        def binarySearch(newIndex):
            newNum = nums[newIndex]
            left, right = 0, newIndex
            ans = newIndex

            while left<=right:
                mid = (left+right)//2
                if nums[mid] == newNum:
                    ans = min(ans, mid)
                    right = mid-1

                else:
                    requiredSum = (newIndex-mid) * newNum
                    currSum = prefix[newIndex] - prefix[mid]
                    if currSum + k >= requiredSum:
                        ans = min(ans, mid)
                        right = mid-1
                    else:
                        left = mid+1

            return newIndex-ans+1

        maxWidth = 1
        for newIndex in range(n):
            width = binarySearch(newIndex)
            maxWidth = max(maxWidth, width)
        return maxWidth

            


                
