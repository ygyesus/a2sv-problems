# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        x = startValue
        ops = 0
        
        if x==target:
            return ops

        if target%2:
            target += 1
            ops += 1

        while target>x:
            if target%2:
                target += 1
                ops += 1
            target //= 2
            ops += 1

        ops += x-target
        return ops