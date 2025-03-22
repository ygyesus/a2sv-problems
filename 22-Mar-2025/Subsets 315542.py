# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generateBitStrings(length):
            LIST = [""]
            
            lengthToString = defaultdict(list)
            lengthToString [0] = ['']
            
            
            for i in range(1, length+1):
                prevStrings = lengthToString[i-1]
                
                for prevString in prevStrings:
                    lengthToString[i].append(prevString+'0')
                    lengthToString[i].append(prevString+'1')
                
                

            # print(dict(lengthToString))
            return lengthToString

        length = len(nums)

        LIST = generateBitStrings(length)[length]    

        ans = []
        for bits in LIST:
            temp = []
            for i, bit in enumerate(bits):
                if int(bit):
                    temp.append(nums[i])


            ans.append(temp)

        return ans