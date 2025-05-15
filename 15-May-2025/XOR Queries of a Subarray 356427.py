# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        prefix = [arr[0]]

        for i in range(1, len(arr)):
            total = prefix[-1] ^ arr[i]
            prefix.append(total)

        answer = []
        for left, right in queries:
            ans = prefix[right] ^ prefix[left] ^ arr[left]
            answer.append(ans)

        return answer