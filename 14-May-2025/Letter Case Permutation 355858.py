# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        ans = []
        for mask in range(1<<len(s)):

            arr = list()
            for i in range(len(s)):
                if mask>>i & 1:
                    arr.append(s[i])
                else:
                    arr.append(s[i].swapcase())

            ans.append(''.join(arr))

        ans = list(set(ans))
        # print(ans)
        return ans
                