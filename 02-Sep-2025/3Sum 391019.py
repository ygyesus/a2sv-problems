# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)

        nums = set(nums)

        ans = set()
        for i in nums:
            for j in nums:
                k = 0 - (i+j)
                if not k in nums: continue
                arr = [i,j,k]
                flag = True
                for num in arr:
                    if arr.count(num) > count[num]:
                        flag = False
                        break
                if not flag: continue
                ans.add(tuple(sorted(arr)))

        ANS = []
        for TUPLE in ans:
            ANS.append(list(TUPLE))
        return ANS


