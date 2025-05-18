# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        bits = []

        bit = 0
        maximum = max(nums)
        if maximum == 0:
            bits.append(0)
        else: 
            while maximum>>bit:
                bits.append(0)
                bit += 1

        # bits.append(0)

        print(bits)

        left = 0
        ans = 1
        for right in range(len(nums)):
            num = nums[right]

            # increment for all of bitRight
            for bitRight in range(len(bits)):
                if num>>bitRight & 1:
                    bits[bitRight] += 1

            # check all bitFrequency is at max 1
            for bit in range(len(bits)):
                while bits[bit] > 1:
                    # remove left number
                    for bitLeft in range(len(bits)):
                        if nums[left]>>bitLeft & 1:
                            bits[bitLeft] -= 1
                    left += 1
                    
            # print(left, right, "after all is settled")
            # print(bits)
            ans = max(ans, right-left+1)

        return ans


            