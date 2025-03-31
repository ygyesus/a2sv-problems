# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def isValid(path):
            if len(path) != 4:
                return False

            for num in path:
                if len(num)>1 and num[0] == '0':
                    return False
                num = int(num)

                if not 0<=num<=255:
                    return False

            return True

        ans = []

        def backtrack(string, path):


            if string == "":
                if isValid(path):
                    ans.append('.'.join(path))
                return

            for i in range(len(string)+1):
                if not string[:i]:
                    continue
                path.append(string[:i])
                backtrack(string[i:], path)
                path.pop()

        backtrack(s, [])
        # print(ans)
        return ans