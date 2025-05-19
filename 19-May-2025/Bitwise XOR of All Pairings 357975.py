# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        #   XOR(nums1)
        #   for nums2[i]: len(nums1) times (XOR(nums2[i]))


        '''
        FOR num in nums1:
            len(nums2) * XOR(num)

        FOR num in nums2:
            len(nums1) * XOR(num)
        '''

        cumulative1 = 0
        if len(nums2)%2 == 1:
            for num in nums1:
                cumulative1 ^= num

        cumulative2 = 0
        if len(nums1)%2 == 1:
            for num in nums2:
                cumulative2 ^= num

        return cumulative1 ^ cumulative2
        


