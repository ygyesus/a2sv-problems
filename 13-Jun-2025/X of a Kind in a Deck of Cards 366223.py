# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        values = Counter(deck).values()
        values = list(values)
        GCD = values[0]

        for i in range(1, len(values)):
            GCD = gcd(GCD, values[i])

        return GCD>1