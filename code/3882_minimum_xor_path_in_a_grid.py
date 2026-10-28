# Problem: Minimum XOR Path in a Grid
# Topic: Dynammic programming
# Difficulty: Medium
from functools import cache


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        @cache
        def dp(i, j) -> set:
            if i == 0 and j == 0:
                return {grid[0][0]}
            ans = set()
            # from left or from top
            if i > 0:
                left = dp(i - 1, j)
                for x in left:
                    ans.add(x ^ grid[i][j])
            if j > 0:
                top = dp(i, j - 1)
                for x in top:
                    ans.add(x ^ grid[i][j])
            return ans

        return min(dp(len(grid) - 1, len(grid[0]) - 1))
