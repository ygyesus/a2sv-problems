# Problem: Count Complete Subarrays in an Array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        distinct = len(set(nums))
        n = len(nums)
        left = 0
        counter = Counter()
        for right in range(len(nums)):
            counter[nums[right]] += 1

            while len(counter) == distinct:

                ans += n-right
                counter[nums[left]] -= 1
                if not counter[nums[left]]:
                    del counter[nums[left]]

                left += 1

        return ans
