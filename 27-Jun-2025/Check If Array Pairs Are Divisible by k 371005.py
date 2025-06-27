# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        counter = Counter()

        for num in arr:
            if num%k==0: 
                
                if 0 in counter:
                    counter[0] -= 1
                    if not counter[0]: del counter[0]
                else: counter[0] += 1
                
                continue
            
            if k - num%k in counter:
                counter[k-num%k] -= 1
                if counter[k-num%k] == 0:
                    del counter[k-num%k]

            else:
                counter[num%k] += 1

        return not counter
