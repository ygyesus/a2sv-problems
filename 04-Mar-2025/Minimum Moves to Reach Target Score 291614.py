# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        def func(target, maxDoubles):
            ans = 0
            if target%2 == 0:
                minEven = target
            else:
                ans += 1
                minEven = target - 1
            
            print("EVENIFY:", ans)
            print("minEven:", minEven)
            doubled = 0
            while maxDoubles and minEven > 1 and minEven%2 == 0:
                minEven //= 2
                maxDoubles -= 1
                doubled += 1
            ans += doubled
            if minEven and maxDoubles:
                return ans + func(minEven, maxDoubles)
            else:
                ans += minEven - 1

            return ans

        return func(target, maxDoubles)