# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        totalTime = 0
        while True:
            for i in range(len(tickets)):

                if i==k:
                    if tickets[i]>0:
                        tickets[i] -= 1
                        totalTime += 1
                    if tickets[i]==0:
                        return totalTime

                    continue
            
                if tickets[i]>0:
                    tickets[i] -= 1
                    totalTime += 1

        
