# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        maxDiff = 0
        length = 0
        maxLength = maxIndex = 0
        netGas = 0


        n = len(gas)

        for i in range(2*n):
            
            i = i%n

            netGas += gas[i] - cost[i]
            # print(i, netGas)

            if netGas < 0:
                length = 0
                netGas = 0
            else:
                length += 1
                if length > maxLength:
                    maxLength = length
                    maxIndex = i
                    # print(maxIndex, maxLength)
            # print("========")


        if maxLength >= n:
            return (maxIndex-maxLength+1)%n
        return -1