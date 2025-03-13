# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def nextBits(prev,n):
            # print(n,prev)
            if n==1:
                # print(prev)
                return prev
            invertedPrev = ''.join([str(1-int(x)) for x in prev])
            reverse = invertedPrev[::-1]

            ans = prev + '1' + reverse
            
            return nextBits(ans, n-1)

        string = nextBits('0', n)

        return string[k-1]