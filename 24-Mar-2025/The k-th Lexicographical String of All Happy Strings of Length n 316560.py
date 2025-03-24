# Problem: The k-th Lexicographical String of All Happy Strings of Length n - https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def generateList(n):
            
            DICT = defaultdict(list)


            DICT[1] = [
                'a', 'b', 'c'
            ]

            
            count = 1

            while count < n:

                for string in DICT[count]:
                    if string[-1] == 'a':
                        DICT[count+1].append(string+'b')
                        DICT[count+1].append(string+'c')

                    elif string[-1] == 'b':
                        DICT[count+1].append(string+'a')
                        DICT[count+1].append(string+'c')
                    elif string[-1] == 'c':
                        DICT[count+1].append(string+'a')
                        DICT[count+1].append(string+'b')

                count += 1

            print(DICT[n])
            return DICT[n]

        LIST = generateList(n)
        k-=1

        if k>= len(LIST):
            return ""

        return LIST[k]

        
