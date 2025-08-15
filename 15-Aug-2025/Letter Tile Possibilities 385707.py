# Problem: Letter Tile Possibilities - https://leetcode.com/problems/letter-tile-possibilities/description/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        paths = []
        def backtrack(path):
            paths.append(path[:])
            if len(path)==len(tiles): return
            for i in range(len(tiles)):
                if i in path: continue
                path.append(i)
                backtrack(path)

                path.pop()
        backtrack([])
        ans = set()
        for path in paths:
            chars = []
            for i in path:
                chars.append(tiles[i])

            string = ''.join(chars)
            if string: ans.add(string)

        return len(ans)

