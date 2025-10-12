# Problem: Minimum Consecutive Cards to Pick Up - https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cardToIndices = defaultdict(list)

        n = len(cards)

        for i, card in enumerate(cards):
            cardToIndices[card].append(i)

        ans = -1
        for card in cardToIndices:
            indices = cardToIndices[card]
            for i in range(1, len(indices)):

                diff = indices[i] - indices[i-1] + 1
                if ans == -1:
                    ans = diff
                else:
                    ans = min(ans, diff)

        return ans
