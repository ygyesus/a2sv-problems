# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class Page:
    def __init__(self, page: str):
        self.page = page
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Page(homepage)
        self.current = self.homepage
        self.current.next = None
        self.steps = 0
    def visit(self, url: str) -> None:
        self.current.next = Page(url)
        self.current.next.prev = self.current
        
        self.current = self.current.next
        self.current.next = None
        self.steps += 1

    def back(self, steps: int) -> str:

        while steps and self.current != self.homepage:
            self.current = self.current.prev
            steps -= 1

        return self.current.page

        

    def forward(self, steps: int) -> str:
        while steps and self.current.next:
            self.current = self.current.next
            steps -= 1

        return self.current.page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)