# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.startOfToken = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.startOfToken[tokenId] = currentTime


    def renew(self, tokenId: str, currentTime: int) -> None:
        if not tokenId in self.startOfToken:
            return
        
        start = self.startOfToken[tokenId] 

        age = currentTime-start
        if age >= self.timeToLive:
            del self.startOfToken[tokenId]
        else:
            self.startOfToken[tokenId] = currentTime


    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0

        for tokenId in self.startOfToken:
            start = self.startOfToken[tokenId]

            age = currentTime-start
            if not (age >= self.timeToLive):
                count += 1

        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)