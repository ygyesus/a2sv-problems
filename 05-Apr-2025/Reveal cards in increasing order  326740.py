# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        n = len(deck)
        
        sortedDeck = sorted(deck)

        sortedIndices = [x for x in range(n)]
        sortedIndices = deque(sortedIndices)

        visitedIndices = []

        while sortedIndices:
            
            visited = sortedIndices.popleft()
            visitedIndices.append(visited)

            if sortedIndices:
                sortedIndices.append(sortedIndices.popleft())

        # print(visitedIndices)

        ans = [0]*n

        for i in range(n):
            trueIndex = visitedIndices[i]
            ans[trueIndex] = sortedDeck[i]

        # print(ans)
        return ans

            
