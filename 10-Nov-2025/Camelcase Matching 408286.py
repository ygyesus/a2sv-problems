# Problem: Camelcase Matching - https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        ans = []
        for query in queries:
            pattern_index = query_index = 0

            while pattern_index<len(pattern) and query_index<len(query):
                if pattern[pattern_index] == query[query_index]: 
                    pattern_index += 1
                    query_index += 1
                else:
                    if not 'a'<=query[query_index]<='z': break
                    else: query_index += 1

            ans.append(pattern_index>=len(pattern))

            while query_index<len(query):
                if not 'a'<=query[query_index]<='z':
                    ans[-1] = False
                    break

                query_index += 1


        return ans