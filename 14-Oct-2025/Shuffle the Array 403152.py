# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []

        x, y = 0, n

        while x<n:
            ans.append(nums[x])
            ans.append(nums[y])

            x += 1
            y += 1

        return ans
            