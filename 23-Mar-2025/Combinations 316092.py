# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def generateBitStrings(length):
            DICT = defaultdict(list)
            DICT[0] = ['']
            

            for curr in range(1, length+1):
                newList = DICT[curr]
                prev = curr-1

                for string in DICT[prev]:
                    newList.append(string + '0')
                    newList.append(string + '1')


            return DICT

        DICT = generateBitStrings(n)
        # print(DICT)

        LIST = DICT[n]
        # print(LIST)

        ans = []
        for string in LIST:
            arr = []
            for i,char in enumerate(string):
                if int(char):
                    arr.append(i+1)

            if len(arr) == k:
                ans.append(arr)


        return ans

                    
