# Problem: Magic Squares In Grid - https://leetcode.com/problems/magic-squares-in-grid/

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def func(startRow, startCol):

            SET = {x for x in range(1, 10)}


            totals = -1

            # Each row's sum
            for row in range(startRow, startRow+3):
                total = 0
                for col in range(startCol, startCol+3):
                    if not grid[row][col] in SET: return False
                    SET.remove(grid[row][col])
                    total += grid[row][col]

                if totals != -1 and totals != total: return False
                totals = total

            # Each col's sum
            for col in range(startCol, startCol+3):
                total = 0
                for row in range(startRow, startRow+3):
                    total += grid[row][col]

                if totals != total: return False

            # Each diagonal's sum

            total = 0
            for diff in range(3):
                total += grid[startRow+diff][startCol+diff]

            if totals != total: return False

            total = 0
            for diff in range(3):
                total += grid[startRow+(2-diff)][startCol+diff]
                
            if totals != total: return False
            
            return True
        
        ans = 0

        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            if not row+2<rows: continue
            for col in range(cols):
                if not col+2<cols: continue
                ans += func(row, col)

        return ans