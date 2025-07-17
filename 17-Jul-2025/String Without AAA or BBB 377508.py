# Problem: String Without AAA or BBB - https://leetcode.com/problems/string-without-aaa-or-bbb

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        while a and b:
            if a>b:
                if not(len(ans)>=2 and ans[-2:] == ['a', 'a']):
                    ans.append('a')
                    a -= 1
                else:
                    ans.append('b')
                    b -= 1
            else:
                if not(len(ans)>=2 and ans[-2:] == ['b', 'b']):
                    ans.append('b')
                    b -= 1    
                else:
                    ans.append('a')
                    a -= 1

        while a:
            ans.append('a')
            a -= 1
        while b:
            ans.append('b')
            b -= 1

        return ''.join(ans)