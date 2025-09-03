# Problem: 4Sum - https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        count = Counter(nums)
        n = len(nums)
        nums = set(nums)
        ans = set()

        
        for a in nums:
            for b in nums:
                for c in nums:
                    d = target-(a+b+c)
                    if not d in nums: continue
                    arr = [a,b,c,d]
                    flag = True
                    for num in arr:
                        if arr.count(num) > count[num]:
                            flag = False
                            break

                    if not flag: continue
                    ans.add(tuple(sorted(arr)))

        return list(ans)
