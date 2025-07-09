# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        for num in counter1:
            if num in counter2:
                for i in range(min(counter1[num], counter2[num])):
                    ans.append(num)

        return ans