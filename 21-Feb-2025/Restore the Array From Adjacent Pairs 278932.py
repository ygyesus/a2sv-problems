# Problem: Restore the Array From Adjacent Pairs - https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) == 1:
            return adjacentPairs.pop()

        neighborsOf = defaultdict(set)

        for x,y in adjacentPairs:
            neighborsOf[x].add(y)
            neighborsOf[y].add(x)

        n = len(adjacentPairs)+1

        ans = [None for _ in range(n)]

        for num in neighborsOf:
            if len(neighborsOf[num]) == 1:
                if ans[0] == None:
                    ans[0] = num
                    continue
                ans[-1] = num
                break

        ans[1] = neighborsOf[ans[0]].pop()
        ans[-2] = neighborsOf[ans[-1]].pop()

        del neighborsOf[ans[0]]
        del neighborsOf[ans[-1]]

        i=2
        j=len(ans)-3

        while i<j:
            # LEFT

            while neighborsOf[ans[i-1]]:
                x = neighborsOf[ans[i-1]].pop()
                if x!=ans[i-2]:
                    ans[i] = x
                    break

            while neighborsOf[ans[j+1]]:
                x = neighborsOf[ans[j+1]].pop()
                if x!=ans[j+2]:
                    ans[j] = x
                    break

            i+=1
            j-=1

        if i==j:
            mySet = neighborsOf[ans[i-1]] & neighborsOf[ans[i+1]]
            ans[i] = mySet.pop()
        return ans