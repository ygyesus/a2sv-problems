# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self, emails):
        self.root = {email: email for email in emails}
        self.rank = {email: 0 for email in emails}

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
            self.root[x] = self.root[self.root[x]]

        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty: return

        rankx = self.rank[rootx]
        ranky = self.rank[rooty]

        if rankx > ranky:
            self.root[rooty] = rootx
        elif ranky > rankx:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
                Account = [
                    name,
                    emails...
                ]
        '''
        emails = set()
        emailToName = defaultdict(str)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                emails.add(email)
                emailToName[email] = name

        dsu = UnionFind(emails)
        
        for account in accounts:
            for j in range(2, len(account)):
                email1 = account[j-1]
                email2 = account[j]

                dsu.union(email1, email2)

        ans = defaultdict(list)
        for email in emails:
            root = dsu.find(email)

            ans[root].append(email)


        lastAns = []
        for value in ans.values():
            name = emailToName[value[0]]
            value = sorted(list(value))

            LIST = list()
            LIST.append(name)
            LIST.extend(value)
            lastAns.append(LIST)

        return lastAns
        

