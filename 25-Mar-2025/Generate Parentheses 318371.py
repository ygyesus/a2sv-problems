# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generateBitString(n):
            DICT = defaultdict(list)
            DICT[0] = ['']

            for curr in range(1, n+1):
                prev = curr-1

                for string in DICT[prev]:
                    DICT[curr].append(string + '1')
                    DICT[curr].append(string + '0')
                print(DICT, curr)

            return DICT

        DICT = generateBitString(2*n)
        # print(dict(DICT))
        LIST = DICT[2*n]


        ans = []

        for string in LIST:
            openBrackets = closedBrackets = 0

            flag = True
            for char in string:
                if not int(char):
                    openBrackets += 1
                else:
                    closedBrackets += 1

                if closedBrackets > openBrackets:
                    flag = False
                    break

            if not flag:
                continue
            if not openBrackets == closedBrackets:
                continue

            ansMember = ''
            for char in string:
                if not int(char):
                    ansMember += '('
                else:
                    ansMember += ')'
                    
            ans.append(ansMember)

        return ans
            
