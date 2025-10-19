# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = Counter(s)

        heap = []
        heapify(heap)

        for char, count in counter.items():
            heappush(heap, (-count, char))

        ans = ['' for _ in range(len(s))]

        for i in range(len(s)):
            if not heap: continue
            count, char = heappop(heap)
            if i>0 and ans[i-1] == char:
                if heap:
                    secondCount, secondChar = heappop(heap)
                    ans[i] = secondChar
                    secondCount += 1
                    if secondCount:
                        heappush(heap, (secondCount, secondChar))
                    heappush(heap, (count, char))
                else:
                    return ''
            else:
                ans[i] = char
                count += 1
                if count:
                    heappush(heap, (count, char))

        return ''.join(ans)
