# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        counter = Counter()

        for num in arr:
            counter[num%k] += 1
        # print(dict(counter))
        for r in counter:
            if r==0: continue
            if not counter[r] == counter[k-r]: 
                print(r, k-r)
                return False

        # print(counter)
        return counter[0]%2==0